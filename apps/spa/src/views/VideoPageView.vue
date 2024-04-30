<script setup lang="ts">
import { useRoute } from 'vue-router'
import { client } from '../api'
import { ref } from 'vue'

import MainLayout from '../layouts/MainLayout.vue'

const route = useRoute()

type Video = {
  id: number
  title: string
  description: string
  video: string
  created_at: string
  updated_at: string
}

const page = ref(Number(route.params.id))
const hasNext = ref(false)

const videos = ref<Video[]>([])

const loadVideo = async () => {
  const { data, error } = await client().GET('/api/videos/', {
    params: { query: { limit: 1, offset: page.value - 1 } }
  })

  if (error) {
    return alert('Failed to load videos')
  }

  videos.value = data.results
  if (data.next) {
    hasNext.value = true
  } else {
    hasNext.value = false
  }
}

await loadVideo()

const sharePage = () => {
  const url = window.location.href
  const shareUrl = `${url}?page=${page.value}`
  navigator.clipboard.writeText(shareUrl)
  alert('Page link copied to clipboard!')
}
</script>

<template>
  <MainLayout>
    <main>
      <button @click="sharePage">Share</button>
      <section>
        <div v-for="video in videos" :key="video.id">
          <h2>{{ video.title }}</h2>
          <p>{{ video.description }}</p>
          <video :src="video.video" controls></video>
        </div>
        <div>
          <button
            @click="$router.push({ name: 'video', params: { id: page - 1 } })"
            v-show="page > 1"
          >
            Previous
          </button>
          <button
            @click="$router.push({ name: 'video', params: { id: page + 1 } })"
            v-show="hasNext"
          >
            Next
          </button>
        </div>
      </section>
    </main>
  </MainLayout>
</template>

<style scoped>
video {
  width: 100%;
  max-width: 500px;
  height: auto;
}

main {
  margin: 0 auto;
}
</style>
