<template>
    <v-app>
        <v-container>
            <H3 class="text-center">Control the displayed data using a table and datetime range filter</H3>
            <router-view/>
        </v-container>
    </v-app>
</template>

<script>
    export default {
        name: 'App',
    };
</script>
