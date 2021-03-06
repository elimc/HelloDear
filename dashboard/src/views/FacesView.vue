<template>
  <card-widget :title="title">
    <div class="flex flex-col mb-5">
      <image-widget :image="image" :loading="loading" class="self-center"></image-widget>
      <div class="mt-10 text-xl text-slate-500">
        Try to choose a face that looks like a realistic selfie (smiling,
        looking at the camera, etc.). You can adjust the age/gender so as to
        find the best fitting image. When you're done, select "Use this face."
      </div>
      <div class="mt-10">
        <h3 class="font-bold text-xl">Generate a new face</h3>
        <ul class="mt-6 flex flex-col gap-5">
          <li class="text-lg font-semibold">Gender</li>
          <li class="flex flex-wrap justify-start gap-4 text-md">
            <div class="flex items-center">
              <input
                class="mr-2 h-4 w-4"
                type="radio"
                name="gender"
                @click="gender = 'female'"
              />
              <label for="gender">Female</label>
            </div>
            <div class="flex items-center">
              <input
                class="mr-2 h-4 w-4"
                type="radio"
                name="gender"
                @click="gender = 'male'"
              />
              <label for="gender">Male</label>
            </div>
          </li>
          <li class="text-lg font-semibold">Age</li>
          <li class="flex flex-wrap justify-start gap-4 text-md">
            <div class="flex items-center">
              <label for="min-age">Minimum</label>
              <input
                class="
                  w-full
                  ml-2
                  px-6
                  py-2
                  bg-transparent
                  border-2 border-cyan-800
                  rounded-md
                "
                type="number"
                v-model="minAge"
                name="min-age"
              />
            </div>
            <div class="flex items-center">
              <label for="max-age">Maximum</label>
              <input
                class="
                  w-full
                  ml-2
                  px-6
                  py-2
                  bg-transparent
                  border-2 border-cyan-800
                  rounded-md
                "
                type="number"
                v-model="maxAge"
                name="max-age"
              />
            </div>
          </li>
          <li class="flex gap-4">
            <button-widget
              @click="state.face && (image = state.face)"
              :disabled="!state.face || image == state.face"
              class="bg-slate-300 disabled:hover:scale-100 disabled:opacity-70"
              >Revert</button-widget
            >
            <button-widget
              @click="slowFetch(gender, minAge, maxAge)"
              class="bg-zinc-400"
              >Regenerate</button-widget
            >
          </li>
        </ul>
      </div>
      <button-widget class="bg-blue-400" @click="submit">
        Use this face
      </button-widget>
    </div>
  </card-widget>
</template>

<script>
import { inject, ref, watch } from "vue";
import CardWidget from "../components/Card.vue";
import ButtonWidget from "../components/Button.vue";
import { debounce } from "lodash";
import { fetchImageUrl } from "../composables/face-fetch";
import ImageWidget from "../components/Image.vue";

export default {
  name: "Faces",
  setup() {
    const title = ref("Faces");
    const state = inject("state");

    const image = ref(state.value.face);
    const loading = ref(true);

    const gender = ref();
    const minAge = ref();
    const maxAge = ref();

    // Fetches an images with specified attributes, but is throttled to 1 call per 500ms so as to not use too many resources.
    const slowFetch = debounce((gender, minAge, maxAge) => {
      loading.value = true;
      fetchImageUrl(gender, minAge, maxAge)
        .then(({ img }) => {
          if (img) {
            image.value = img;
          }
        })
        .finally(() => (loading.value = false));
    }, 500);

    // Load image initially if none in state.
    if (!image.value) {
      slowFetch();
    } else {
      loading.value = false;
    }

    // Watch for changes in gender, minAge, or maxAge and update image accordingly
    watch([gender, minAge, maxAge], () =>
      slowFetch(gender.value, minAge.value, maxAge.value)
    );

    // Save image to state.
    const submit = () => {
      if (image.value) {
        state.value.face = image.value;
      }
    };

    return {
      title,
      state,
      image,
      loading,
      gender,
      minAge,
      maxAge,
      slowFetch,
      submit,
    };
  },
  components: { CardWidget, ButtonWidget, ImageWidget },
};
</script>
