<template>
  <card-widget :title="title">
    <h3 class="text-xl text-slate-500 leading-loose">
      HelloDear is an open-source AI built for the 2022 Austin Community College
      RiverHacks hackathon. Designed to combat the multi-billion dollar romance
      scam industry, HelloDear wastes as much of a scammer's time as possible,
      by pretending to be interested, leading them on as long as possible. Every
      minute they spend talking to HelloDear is a minute not scamming a real
      person, and we aim to raise this as high as we can, so as to reduce
      scammers' success rates as much as possible.
    </h3>
  </card-widget>
</template>

<script>
import { inject, ref } from "vue";
import CardWidget from "../components/Card.vue";

export default {
  name: "About",
  setup() {
    const title = ref("About");
    const state = inject("state");

    return { title, state };
  },
  components: { CardWidget },
};
</script>
