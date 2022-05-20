<template>
  <card-widget :title="title">
    <div v-for="field in fields" :key="field.key" class="mb-5">
      <label class="pr-3 uppercase font-bold" :for="field.label">
        {{ field.label }}
      </label>
      <br />
      <input
        type="text"
        :name="field.label"
        pattern="^\d+$"
        :value="field.value"
        @input="
          ({ target }) =>
            target.validity.valid ? (field.value = target.value) : {}
        "
        class="
          px-6
          py-2
          bg-transparent
          border-2 border-cyan-800
          rounded-xl
          invalid:border-red-600
          valid:border-green-600
        "
      />
    </div>
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
      @click="submit"
    >
      Save
    </button>
  </card-widget>
</template>

<script>
import { inject, ref } from "vue";
import CardWidget from "../components/Card.vue";

export default {
  name: "Home",
  setup() {
    const title = ref("Configuration");
    const state = inject("state");
    const fields = ref([
      {
        label: "Message ID",
        key: "messageID",
        pattern: /^\d+$/,
        value: state.value.messageID,
      },
    ]);
    const submit = () => {
      fields.value.forEach(({ key, value }) => {
        if(value) {
          state.value[key] = value;
        }
      });
    };
    return { title, state, fields, submit };
  },
  components: { CardWidget },
};
</script>
