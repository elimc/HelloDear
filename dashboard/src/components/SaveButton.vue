<template>
  <button
    class="
      self-end
      mt-10
      px-5
      py-2
      bg-blue-500
      font-semibold
      rounded-lg
      hover:scale-105
      transition-all
    "
  >
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "SaveButton"
};
</script>