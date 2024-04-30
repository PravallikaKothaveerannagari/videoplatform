<template>
  <div>
    <div v-if="response.ok">
      <p>Activation complete, please login now</p>
      <RouterLink to="/login">Login</RouterLink>
    </div>
    <div v-else>
      <p>An error occurred</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { client } from '@/api'
import { useRoute } from 'vue-router'

const { response } = await client().POST('/auth/users/activation/', {
  body: {
    token: useRoute().params.token as string,
    uid: useRoute().params.uid as string
  }
})
</script>
