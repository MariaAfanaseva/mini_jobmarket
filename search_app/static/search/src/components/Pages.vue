<template>
    <div class="pages">
        <div class="page-number" v-for="page in totalPages" :key="page" >
            <div v-if="page" v-on:click="changePage(page)">
                {{ page }}
            </div>
            <div v-else>
                ...
            </div>
        </div>
    </div>
</template>

<script>
    export default {
      name: 'Pages',
      props: {
        totalPages: Array,
        searchLine: String,
        },

      methods: {
          changePage(page) {
              this.$router.push({ path: '/search-job',
                  query: { keywords: this.searchLine, page: page } });
          }
      }
    }
</script>

<style scoped>

    .pages {
        display: flex;
        justify-content: center;
    }

    .page-number {
        padding: 8px;
    }

</style>
