<template>
  <div class="home">
     <div>
        <input placeholder="Search" type="text" v-model="searchLine">
        <button type="submit" @click="changePage">Search</button>
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
        },

        getData(page=1) {
            let url = 'http://127.0.0.1:5000/search?page=' + page;
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
