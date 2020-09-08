<template>
    <v-container>
        <v-row justify="center">
            <v-col
                    cols="4"
            >
                <p>Hide/Show Columns</p>

                <v-btn-toggle
                        v-model="toggle_multiple"
                        dense
                        color="success"
                        background-color="red"
                        multiple
                >
                    <v-btn>
                        time
                    </v-btn>

                    <v-btn>
                        gaze_x
                    </v-btn>

                    <v-btn>
                        gaze_y
                    </v-btn>

                    <v-btn>
                        key
                    </v-btn>

                    <v-btn>
                        mouse_dx
                    </v-btn>

                    <v-btn>
                        mouse_dy
                    </v-btn>

                    <v-btn>
                        mouse_key
                    </v-btn>
                </v-btn-toggle>
            </v-col>
        </v-row>
        <v-row align="start" justify="center">
            <v-data-table
                    caption="Gamer Activity"
                    dense
                    :multi-sort="true"
                    :headers="headers"
                    :items="actions"
                    :options.sync="options"
                    :server-items-length="totalActions"
                    :loading="loading"
                    class="elevation-1 ma-2"
            >
                <template v-slot:item.keys="{ item }">
                    <v-btn v-for="button in item.keys" :key="button.id" rounded x-small color="primary"> {{ button.key
                        }}
                    </v-btn>
                </template>
                <template v-slot:item.mouse_keys="{ item }">
                    <v-btn v-for="button in item.mouse_keys" :key="button.id" rounded x-small color="primary"> {{
                        button.mouse_key }}
                    </v-btn>
                </template>
            </v-data-table>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "DataTable",
        props: {
            table_data: {
                type: Array
            },
            total: {
                type: Number
            },
            page: {
                type: Number
            }
        },
        data() {
            return {
                toggle_multiple: [0, 1, 2, 3, 4, 5, 6],
                baseHeaders: [
                    {
                        text: 'time',
                        align: 'start',
                        value: 'time',
                        sortable: false
                    },
                    {text: 'gaze_x', value: 'gaze_x', sortable: false},
                    {text: 'gaze_y', value: 'gaze_y', sortable: false},
                    {text: 'keys', value: 'keys', sortable: false},
                    {text: 'mouse_dx', value: 'mouse_dx', sortable: false},
                    {text: 'mouse_dy', value: 'mouse_dy', sortable: false},
                    {text: 'mouse_keys', value: 'mouse_keys', sortable: false},
                ],
                options: {
                    search: '',
                    itemsPerPage: 10,
                    page: 1,
                    sortBy: [],
                },
                loading: false,
            }
        },
        watch: {
            'options.page': {
                handler: function (newVal, oldVal) {
                    if (newVal != oldVal) {
                        this.$emit('change-pagination', newVal, this.options.itemsPerPage);
                    }
                },
                deep: true
            },
            // 'options.search': {
            //     handler: function(newVal, oldVal) {
            //     if (newVal != oldVal) {
            //         }
            //     },
            //     deep: true
            // },
            'options.itemsPerPage': {
                handler: function (newVal, oldVal) {
                    if (newVal != oldVal) {
                        this.$emit('change-pagination', this.options.page, this.options.itemsPerPage);
                    }
                },
                deep: true
            },
            // 'options.sortBy': {
            //     handler: function(newVal, oldVal) {
            //     if (newVal != oldVal) {
            //         }
            //     },
            //     deep: true
            // },
        },
        computed: {
            actions() {
                return this.table_data ? this.table_data : []
            },
            totalActions() {
                return this.total ? this.total : 0
            },
            headers() {
                let computedHeaders = this.toggle_multiple.map((item) => this.baseHeaders[item]);
                return computedHeaders
            },
        }
    }
</script>

<style scoped>

</style>