<template>
    <v-container>
        <DateTimePicker
                @update-time-range="updateTableTimeRange"
                @apply-new-dateTime="getActions"
        ></DateTimePicker>
        <v-row justify="center">
            <Charts
                    :charDataGazeProp="charDataGazeProp"
                    :charDataMouseProp="charDataMouseProp"
            ></Charts>
            <DataTable
                    :table_data="gamerActions"
                    :total="total"
                    :page="page"
                    @change-pagination="updateGamerActions"
            ></DataTable>
        </v-row>
    </v-container>
</template>

<script>
    import DateTimePicker from "../components/DateTimePicker";
    import Charts from "../components/Charts";
    import DataTable from "../components/DataTable";
    import axios from "../plugins/api.service";

    export default {
        name: 'Home',
        data() {
            return {
                page: 1,
                per_page: 10,
                mouse_activity: null,
                gaze_activity: null,
                gamerActions: null,
                pages: null,
                startDateTime: null,
                endDateTime: null,
                total: 0,
                charDataGazeProp: [],
                charDataMouseProp: [],
            }
        },
        components: {
            DateTimePicker, Charts, DataTable
        },
        mounted() {
            // upload data after component mounted
            this.getActions()
        },
        methods: {
            // upload data - array of gamer actions from backend
            getActions() {
                axios.get('/', {
                    params: {
                        // query parameter: start - datetime interval start (type String),
                        // end - datetime interval end (type String)
                        // pre_page, page - pagination parameter
                        per_page: this.per_page,
                        page: this.page,
                        start: this.startDateTime,
                        end: this.endDateTime,
                    }
                }).then((response) => {
                    if (response.status === 200) {
                        // response.data.actions - array of gamer actions
                        this.gamerActions = response.data.actions;
                        // total records by query parameter
                        this.total = response.data.total;
                        // total page pagination
                        this.pages = response.data.pages;
                        // gaze - array for save gaze actions chart parameters
                        // mouse - array for save gaze actions mouse parameters
                        // format [ datetime, X coordinate, Y coordinate, clicked buttons ]
                        let gaze = [];
                        let mouse = [];
                        response.data.actions.forEach(e => {
                            gaze.push([e.time.toString(), e.gaze_x, e.gaze_y, JSON.stringify(e.keys)]);
                            mouse.push([e.time.toString(), e.mouse_dx, e.mouse_dy, JSON.stringify(e.mouse_keys)]);
                        });
                        // update Props for Charts
                        this.charDataGazeProp = gaze;
                        this.charDataMouseProp = mouse;
                    } else {
                        //TODO notification user
                        console.log(`error response ${response.status}`)
                    }
                })
            },
            updateTableTimeRange(start, end) {
                // update startDateTime and endDateTime from DateTimePicker component
                this.startDateTime = start;
                this.endDateTime = end;
            },
            updateGamerActions(page, per_page) {
                // update gamer actions on change page or per_page in table
                this.page = page;
                this.per_page = per_page;
                this.getActions();
            },

        }
    }
</script>
