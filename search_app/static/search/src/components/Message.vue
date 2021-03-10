<template>
    <div>
        <div v-show="isVisible">
            Für Deine Suche haben wir keine aktuelle Stellenangebote gefunden.
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Message',
        props: {
            isVisible: Boolean,
        },
    }
</script>
