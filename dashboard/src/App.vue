<template>
  <tabs-vue :tabs="tabs">
    <router-view v-slot="{ Component }" class="p-5 sm:p-10">
      <keep-alive>
        <component :is="Component" />
      </keep-alive>
    </router-view>
  </tabs-vue>
</template>

<script>
import { provide, ref, watch } from "vue";
import TabsVue from "./components/Tabs.vue";

export default {
  components: { TabsVue },
  setup() {
    const tabs = ref([
      {
        name: "Home",
        route: "/home",
      },
      {
        name: "Config",
        route: "/config",
      },
      {
        name: "Faces",
        route: "/faces",
      },
      {
        name: "About",
        route: "/about",
      },
    ]);

    // Very simple global state object.
    // This is not really a good way to manage state,
    // but there's not much time to set up a proper store
    const state = ref({
      messageID: "test",
      face: ""
    });

    // Provide global state so it available in any components if required
    provide("state", state);

    // Watch for updates in the state
    watch(
      state,
      (curr, prev) => {
        console.log("State updated", state.value);
      },
      { deep: true }
    );

    return {
      tabs,
    };
  },
};
</script>
