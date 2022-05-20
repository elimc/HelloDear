<template>
  <div class="flex items-start">
    <ul class="flex flex-col flex-wrap list-none border-b-0 pl-0 mr-4">
      <li v-for="tab in tabs" :key="tab.name" class="flex-grow text-center">
        <router-link :to="tab.route" @click="selected = tab" :class="{ 'bg-blue-300': tab == selected }"
          class="block font-medium text-xl uppercase px-6 py-3 my-2 hover:bg-gray-100">
          {{ tab.name }}
        </router-link>
      </li>
    </ul>
    <div>
      <slot></slot>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: "Tabs",
  setup(props) {
    const selected = ref(props.tabs[0]) // TODO: check if props.tabs is array w/ at least one element.

    return { selected }
  },
  props: {
    tabs: {
      type: Array,
      required: true
    }
  }
}
</script>