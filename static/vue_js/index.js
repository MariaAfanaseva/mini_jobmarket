Vue.component('vacancies', {
    props: {
        jobs: Array
    },

    template:
        '<div>' +
            '<a v-for="job in jobs" :key="job.id" :href="`/jobs/${job.id}`">' +
                '<div v-html="job.title"></div>' +
            '</a>' +
        '</div>'
});

new Vue({
    el: '#root',

    data() {
        return{
            jobs: [],
            searchLine: ''
        }
    },

    created() {
        this.getData();
    },

    methods: {
        getData() {
            let url = 'http://127.0.0.1:5000/search?';
            let keywords = this.searchLine.match(/[^ ]+/g);
            if (keywords) {
                url += '&keyword=' + keywords.join('&keyword=');
            }
            fetch(url)
                .then(res => res.json())
                .then(result => this.jobs = result.jobs)
        }
    }
});
