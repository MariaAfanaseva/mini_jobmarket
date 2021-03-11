<template>
  <div class="jobs-container">
      <a class="job-box" v-for="job in jobs" :key="job.id" :href="'/jobs/' + job.id" target="_blank">
          <div class="job-title" v-html="job.title"></div>
          <div class="location-container">
            <font-awesome-icon icon="map-marker-alt" class="location-logo" />
            <div class="job-location" v-html="job.workplace"></div>
          </div>
      </a>
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

<style scoped>
    .jobs-container {
        display: grid;
        grid-template-columns: auto;
        grid-gap: 10px;
    }

    .job-box {
        padding: 20px 30px;
        border: 1px solid #c2cdd1;
        transition:  box-shadow 0.5s;
    }

    .job-box:link, .job-box:visited {
        text-decoration: none;
        color: #323131;
    }

    .job-box:hover {
        box-shadow: 2px 4px 10px 0 rgba(1, 1, 1, .5);
    }

    .location-container {
        margin: 10px;
    }
    .job-location {
        margin-top: 6px;
        color: #96a2b2;
        display: inline;
        margin-left: 8px;
    }

    .location-logo {
        color: #96a2b2;
    }

    @media screen and (max-width: 767px) {
        .jobs-container {
            text-align: center;
        }
    }
</style>
