<template>
    <v-container>
        <v-row align="start" justify="center">
            <v-col cols="6">
                <GChart
                        type="BubbleChart"
                        :data="charDataGaze"
                        :options="chartOptionsGaze"
                        :resizeDebounce="800"
                        :events="chartEventsGaze"
                        ref="keyChart"
                />
            </v-col>
            <v-col cols="6">
                <GChart
                        type="BubbleChart"
                        :data="charDataMouse"
                        :options="chartOptionsMouse"
                        :resizeDebounce="800"
                        :events="chartEventsMouse"
                        ref="mouseChart"
                />
            </v-col>
        </v-row>
        <v-snackbar
                v-for="(notify, index) in notifications"
                v-model="snackbar"
                :key="index"
                :timeout="-1"
                :color="notify.color"
                :style="`padding-bottom: ${(index * 60) + 8}px`"
        >
            {{notify.text}}
        </v-snackbar>
    </v-container>
</template>

<script>
    import {GChart} from 'vue-google-charts'

    export default {
        name: "Charts",
        props: {
            charDataGazeProp: {
                type: Array,
            },
            charDataMouseProp: {
                type: Array,
            },
        },
        components: {
            GChart
        },
        data() {
            return {
                notifications: [],
                snackbar: true,
                charDataGazeHead: [
                    ["time", "mouse_dx", "mouse_dy", "mouse_key"],
                ],
                charDataMouseHead: [
                    ["time", "gaze_x", "gaze_y", "key"],
                ],
                chartOptionsGaze: {
                    width: 800,
                    height: 500,
                    title: 'Gamer Gaze Activity',
                    sizeAxis: {minValue: 0, maxSize: 5},
                    legend: {position: 'top', textStyle: {color: 'blue', fontSize: 16}},
                    explorer: {},
                    hAxis: {title: 'mouse_dx'},
                    vAxis: {title: 'mouse_dy'},
                    colorAxis: {colors: ["yellow", "red"]},
                },
                chartOptionsMouse: {
                    width: 800,
                    height: 500,
                    title: 'Gamer Mouse Activity',
                    sizeAxis: {minValue: 0, maxSize: 5},
                    legend: {position: 'top', textStyle: {color: 'blue', fontSize: 16}},
                    explorer: {},
                    hAxis: {title: 'mouse_dx'},
                    vAxis: {title: 'mouse_dy'},
                    colorAxis: {colors: ["yellow", "red"]},
                },
                chartEventsGaze: {
                    select: () => {
                        const chart = this.$refs.keyChart.chartObject;
                        const selection = chart.getSelection();
                        // handle event here
                        if (selection) {
                            if (this.notifications.length === 6) {
                                this.notifications.shift();
                            }
                            this.notifications.push({
                                'color': 'primary',
                                'text': `Выбрано действие ${this.charDataGaze[selection[0]['row']]}.`
                            });
                            setTimeout(() => {
                                this.notifications.shift();
                            }, 3000);
                        }

                    },
                },
                chartEventsMouse: {
                    select: () => {
                        console.log('event')
                        const chart = this.$refs.mouseChart.chartObject;
                        const selection = chart.getSelection();
                        // handle event here
                        if (selection) {
                            if (this.notifications.length === 6) {
                                this.notifications.shift();
                            }
                            this.notifications.push({
                                'color': 'primary',
                                'text': `Выбрано действие ${this.charDataMouse[selection[0]['row']]}.`
                            });
                            setTimeout(() => {
                                this.notifications.shift();
                            }, 3000);
                        }
                    },
                },
            }
        },
        computed: {
            charDataMouse() {
                let mouseArray = this.charDataMouseProp ? this.charDataMouseProp : []
                return this.charDataMouseHead.concat(mouseArray)
            },
            charDataGaze() {
                let gazeArray = this.charDataGazeProp ? this.charDataGazeProp : []
                return this.charDataGazeHead.concat(gazeArray)
            }

        }


    }
</script>

<style scoped>

</style>