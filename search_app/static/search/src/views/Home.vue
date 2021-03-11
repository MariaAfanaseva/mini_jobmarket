<template>
  <div class="home">
     <div class="search-block">
         <input class="search-input" placeholder="Jobtitel, Fähigkeiten oder Firma" type="text" v-model="searchLine">
         <button class="search-btn" type="submit" @click="changePage">Suchen</button>
     </div>
    <Vacancies v-bind:jobs="jobs"></Vacancies>
    <Pages v-bind:total-pages="totalPages" v-bind:search-line="searchLine"></Pages>
    <Message v-bind:is-visible="isVisibleMessage"></Message>
  </div>
</template>

<script>
import Vacancies from '@/components/Vacancies.vue';
import Pages from '@/components/Pages.vue';
import Message from '@/components/Message.vue';

export default {
  name: 'Home',
  components: {
    Vacancies,
    Pages,
    Message
  },

  data() {
        return{
            jobs: [],
            searchLine: '',
            totalPages: [],
            isVisibleMessage: false,
        }
    },

  computed: {
    page() {
      return this.$route.query.page
    }
  },

    created() {
        this.getData();
    },

    watch: {
        jobs: function(val) {
            this.isVisibleMessage = (val.length === 0);
        },

        page: function (val) {
            if (val) {
                this.getData(val);
            }
        }
    },

    methods: {
        scrollToTop() {
            window.scrollTo(0,0);
        },

        changePage() {
              this.$router.push({ path: '/search-job',
                  query: { keywords: this.searchLine, page: 1 } });
              this.getData(1);
        },

        getData(page=1) {
            // Change url
            let url = 'http://192.168.178.44:5000/search?page=' + page;
            let keywords = this.searchLine.match(/[^ ]+/g);
            if (keywords) {
                url += '&keyword=' + keywords.join('&keyword=');
            }
            console.log(url);
            fetch(url)
                .then(res => res.json())
                .then(result => {
                    this.jobs = result.jobs;
                    this.totalPages = result.totalPages;
                    this.scrollToTop();
                });

        }
    }
}
</script>

<style>
    .home {
        margin: 5% 15%;
        display: grid;
        grid-gap: 10px;
    }

    .search-block {
        display: grid;
        grid-template-columns: auto auto auto auto;
        grid-gap: 10px;
        margin: 30px 0 20px 0;
    }

    .search-input {
        border-radius: 5px;
        height: 50px;
        padding-left: 30px;
        border: 1px solid #c2cdd1;
        grid-column-start: 1;
        grid-column-end: 4;
        font-weight: bolder;
    }

    .search-input:focus {
        outline: none;
        border: 1px solid #c2cdd1;
        border-radius: 5px;
    }

    .search-btn {
        border-radius: 5px;
        background: linear-gradient(
                to right, #b9382f, #b9382f, #922A21
        );
        border: none;
        color: #fff;
        font-weight: 900;
    }

    .search-btn:focus{
        outline: none;
    }

    .search-btn:hover{
        cursor: pointer;
        background: linear-gradient(
            to left, #b9382f, #b9382f, #922A21
        );
    }

    @media screen and (max-width: 767px) {
        .home {
            margin: 5% 8%;
        }

        .search-input {
            height: 40px;
            padding-left: 20px;
            grid-column-start: 1;
            grid-column-end: 5;
        }

         .search-btn {
             height: 40px;
             grid-column-start: 1;
             grid-column-end: 5;
        }
    }
</style>
