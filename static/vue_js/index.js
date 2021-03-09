Vue.component('pages', {
    props: {
        totalPages: Array,
    },
    emits: ['update'],

    template:`
        <div class="pages">
            <div class="page-number" v-for="page in totalPages" :key="page" >
                <div v-if="page" v-on:click="$emit('update', page)">
                    {{ page }}
                </div>
                <div v-else>
                    ...
                </div>
            </div>
        </div>
    `
});

Vue.component('vacancies', {
    props: {
        jobs: Array,
    },

    template:`
        <div>
            <div>
                <a v-for="job in jobs" :key="job.id" :href="'/jobs/' + job.id" target="_blank">
                    <div style="padding: 20px;" v-html="job.title"></div>
                </a>
            </div>
        </div>    
    `
});

Vue.component('message', {
    props: {
        isVisible: Boolean,
    },

    template:`
        <div>
            <div v-show="isVisible">
                Für Deine Suche haben wir keine aktuelle Stellenangebote gefunden.
            </div>
        </div>    
    `
});

new Vue({
    el: '#root',

    data() {
        return{
            jobs: [],
            searchLine: '',
            totalPages: [],
            isVisibleMessage: false,
        }
    },

    created() {
        this.getData();
    },

    watch: {
        jobs: function(val) {
            this.isVisibleMessage = (val.length === 0);
        },
    },

    methods: {
        scrollToTop() {
            window.scrollTo(0,0);
        },

        getData(page=1) {
            let url = 'http://127.0.0.1:5000/search?page=' + page;
            console.log(url);
            let keywords = this.searchLine.match(/[^ ]+/g);
            if (keywords) {
                url += '&keyword=' + keywords.join('&keyword=');
            }
            fetch(url)
                .then(res => res.json())
                .then(result => {
                    this.jobs = result.jobs;
                    this.totalPages = result.totalPages;
                    this.scrollToTop();
                });

        }
    }
});
