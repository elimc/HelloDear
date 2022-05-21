<template>
  <div class="flex items-start flex-col md:flex-row">
    <details class="pl-0 mr-4">
      <summary
        class="        
          font-medium
          text-xl
          w-screen
          sm:w-auto
          pl-32
          pr-7
          py-3
          my-2
          text-right
          rounded-r-full
          bg-slate-300
          hover:bg-slate-200
        "
      >
        Menu
      </summary>
      <ul class="flex flex-col flex-wrap list-none">
        <li v-for="tab in tabs" :key="tab.name" class="flex-grow text-center">
          <router-link
            :to="tab.route"
            :class="{
              'bg-blue-300': isTabSelected(tab),
              'hover:bg-blue-200': isTabSelected(tab),
              'hover:bg-gray-200': !isTabSelected(tab)
            }"
            class="
              block
              font-medium
              text-xl
              w-screen
              sm:w-auto
              pl-32
              pr-7
              py-3
              my-2
              text-right
              rounded-r-full              
            "
          >
            {{ tab.name }}
          </router-link>
        </li>
      </ul>
    </details>
    <div class="w-full max-w-5xl">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import { useRoute } from "vue-router";

export default {
  name: "Tabs",
  setup(props) {
    const currRoute = useRoute();
    const isTabSelected = (tab) => {
      const tabName = String(tab.name).toLowerCase();
      const currName = String(currRoute.name).toLowerCase();
      console.log(tab.name, currRoute.name);

      return tabName == currName;
    };

    return { currRoute, isTabSelected };
  },
  props: {
    tabs: {
      type: Array,
      required: true,
    },
  },
};
</script>