<template>
  <div>
      <div>
          <a v-for="job in jobs" :key="job.id" :href="'/jobs/' + job.id" target="_blank">
              <div class="job-title" v-html="job.title"></div>
          </a>
      </div>
  </div>
</template>

<script>
export default {
  name: 'Vacancies',
   props: {
        jobs: Array,
   },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.job-title {
  padding: 20px;
}
</style>
