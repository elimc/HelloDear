<template>
  <div class="w-full">
    <div class="flex flex-col rounded-2xl p-5 sm:p-10 shadow-2xl">
      <h1 class="text-2xl font-extrabold mb-4">{{ title }}</h1>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    title: {
      type: String,
      required: true
    }
  }
};
</script>

<style>
</style>