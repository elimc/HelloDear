<template>
  <div class="flex items-start">
    <ul class="flex flex-col flex-wrap list-none border-b-0 pl-0 mr-4">
      <!-- <li>{{ currRoute.path }} - {{ tab.route }}</li> -->
      <li v-for="tab in tabs" :key="tab.name" class="flex-grow text-center">
        <router-link :to="tab.route" :class="{ 'bg-blue-300': isTabSelected(tab) }"
          class="block font-medium text-xl px-6 py-3 my-2 hover:bg-gray-100">
          {{ tab.name }}
        </router-link>
      </li>
    </ul>
    <div class="w-full max-w-5xl">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import { useRoute } from 'vue-router'

export default {
  name: "Tabs",
  setup(props) {
    const currRoute = useRoute();
    const isTabSelected = (tab) => {
      const tabName = String(tab.name).toLowerCase();
      const currName = String(currRoute.name).toLowerCase();
      console.log(tab.name, currRoute.name)
      
      return tabName == currName;
    }
   
    return { currRoute, isTabSelected }
  },
  props: {
    tabs: {
      type: Array,
      required: true
    }
  }
}
</script>