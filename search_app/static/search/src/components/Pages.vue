<template>
    <div class="pagination-container">
        <router-link v-for="page in totalPages"
                     :key="page"
                     :to="{ path: '/search-job',
                            query: { keywords: searchLine, page: page } }"
                     class="pagination-number">
            <div v-if="page" v-on:click="changePage(page)">
                {{ page }}
            </div>
            <div v-else>
                ...
            </div>
        </router-link>
    </div>
</template>

<script>
    export default {
      name: 'Pages',
      props: {
          totalPages: Array,
          searchLine: String,
          searchLocation: String,
      },

      methods: {
          changePage(page) {
              this.$router.push({ path: '/search-job',
                  query: { keywords: this.searchLine,
                           where: this.searchLocation,
                           page: page } });
          }
      }
    }
</script>

<style scoped>
    .pagination-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        margin: 20px 0;
    }

    .pagination-number {
        color: black;
        text-decoration: none;
        padding: 8px;
        width: 35px;
        text-align: center;
        border: 1px solid #c2cdd1;
        border-right: none;
    }

    .pagination-number:hover {
        cursor: pointer;
        background-color: #b9382f;
        border-color: #b9382f;
    }

    .router-link-exact-active {
        cursor: none;
        background-color: #b9382f;
        border-color: #b9382f;
    }

    .pagination-number:last-child {
        border-right: 1px solid #c2cdd1;
    }

    @media screen and (max-width: 768px) {
        .pagination-number {
            width: 20px;
            padding: 5px;
            margin: 10px 0 20px 0;
        }
    }

</style>
