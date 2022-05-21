import { ref } from 'vue'


export async function fetchImageUrl(gender = undefined, minAge = undefined, maxAge = undefined) {
  const API_URL = new URL("https://fakeface.rest/face/json")

  let imgUrl = "";
  let imgContent = "";

  const url = API_URL;

  const setParam = (name, param) => param !== undefined && url.searchParams.append(name, param);
  setParam('gender', gender);
  setParam('minimum_age', minAge);
  setParam('maximum_age', maxAge);

  try {
    const response = await fetch(url);
    if (response.status == 200) {
      const json = await response.json();
      if (json.image_url) {
        imgUrl = json.image_url;
        const imgBlob = await (await fetch(imgUrl)).blob();
        const reader = new FileReader();
        reader.readAsDataURL(imgBlob);
        imgContent = await new Promise(res => {
          reader.onloadend = () => {
            const base64data = reader.result;
            res(base64data);
          }
        })

      }
    }
  } catch (e) {
    console.error("Unable to get image results:");
    console.error(e)
  }


  return {
    url: imgUrl,
    img: imgContent
  };
}