<template>
  <tabs-vue :tabs="tabs">
    <router-view></router-view>
  </tabs-vue>
</template>

<script>
import { ref } from "vue"
import TabsVue from './components/Tabs.vue'

export default {
  components: { TabsVue },
  setup() {
    const tabs = ref([
      {
        name: "Home",
        route: "/home"
      },
      {
        name: "About",
        route: "/about"
      },

    ])

    return {
      tabs
    }
  }
}
</script>
