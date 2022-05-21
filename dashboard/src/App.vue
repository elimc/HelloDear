<template>
  <div>
    <nav-bar></nav-bar>
    <tabs-vue :tabs="tabs">
      <router-view v-slot="{ Component }" class="px-5 sm:px-10">
        <keep-alive>
          <component :is="Component" />
        </keep-alive>
      </router-view>
    </tabs-vue>
  </div>
</template>

<script>
import { provide, ref, watch } from "vue";
import NavBar from "./components/NavBar.vue";
import TabsVue from "./components/Tabs.vue";

export default {
  components: { TabsVue, NavBar },
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
      messageID: "123456789",
      face: "",
    });

    // Get initial state from API
    fetch("http://127.0.0.1:8000/config").then((resp) =>
      resp.json().then((json) => (state.value = json))
    );

    // Provide global state so it available in any components if required
    provide("state", state);

    // Watch for updates in the state
    watch(
      state,
      (curr, prev) => {
        console.log("State updated", state.value);
        fetch("http://127.0.0.1:8000/config", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(state.value),
        }).then((res) => {
          console.log("State saved", res);
        });
      },
      { deep: true }
    );

    return {
      tabs,
    };
  },
};
</script>
