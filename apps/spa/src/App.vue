<script setup lang="ts"></script>

<template>
  <Suspense>
    <RouterView :key="$route.fullPath" />
  </Suspense>
</template>

<style scoped></style>
