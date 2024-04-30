<script setup lang="ts">
import { client } from '../api'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

import MainLayout from '../layouts/MainLayout.vue'

type Video = {
  id: number
  title: string
  description: string
  video: string
  created_at: string
  updated_at: string
}

const videos = ref<Video[]>([])

const loadVideo = async () => {
  const { data, error, response } = await client().GET('/api/videos/')

  if (error) {
    if ((response as Response).status === 401) {
      return router.push({ name: 'login' })
    }
    return alert('Failed to load videos')
  }

  videos.value = data.results
}

await loadVideo()
</script>

<template>
  <MainLayout>
    <main>
      <section>
        <template v-if="videos.length !== 0">
          <router-link
            :to="{ name: 'video', params: { id: video.id } }"
            v-for="video in videos"
            :key="video.id"
          >
            <h2>{{ video.title }}</h2>
            <p>{{ video.description }}</p>
          </router-link>
          <br />
        </template>
        <template v-else>
          <p>No videos found</p>
        </template>
      </section>
    </main>
  </MainLayout>
</template>

<style scoped>
main {
  margin: 0 auto;
}
</style>
