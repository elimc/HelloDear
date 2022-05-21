<template>
  <card-widget :title="title">
    <div class="mt-10 grid grid-cols-1 gap-12">
      <div class="flex flex-col xl:flex-row justify-between gap-12 p-5 sm:p-10 bg-slate-200 rounded-3xl">
        <div>
          <h2 class="text-2xl font-bold mb-3">Status</h2>
          <p class="text-xl leading-relaxed self-center xl:self-end">
            Here, you can view the status of the AI.
          </p>
        </div>
        <div>Currently unimplemented: Status widget</div>
      </div>
      <div class="flex flex-col xl:flex-row justify-between gap-12 p-5 sm:p-10 bg-slate-200 rounded-3xl">
        <div>
          <h2 class="text-2xl font-bold mb-3">Your "face"</h2>
          <p class="text-xl leading-relaxed">
            This AI-generated picture will be sent to scammers if they ask for a
            picture of you. So, make sure it looks like a realistic selfie that
            a person would take. You can update this face in the Faces tab.
          </p>
        </div>

        <image-widget
          :image="state.face"
          :loading="false"
          loading-text="You don't have an image set up. Go to the Faces page to set one up."
          class="self-center xl:self-end"
        ></image-widget>
      </div>
    </div>
  </card-widget>
</template>

<script>
import { inject, ref } from "vue";
import CardWidget from "../components/Card.vue";
import ImageWidget from "../components/Image.vue";

export default {
  name: "Home",
  setup() {
    const title = ref("Home");
    const state = inject("state");

    return { title, state };
  },
  components: { CardWidget, ImageWidget },
};
</script>
