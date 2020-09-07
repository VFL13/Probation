<template>
  <v-app>
    <v-container>
       <router-view/>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data() {
    return {
      notifications: [],
      snackbar: true,
      headers: [
        {
          text: 'time',
          align: 'start',
          value: 'time',
        },
        { text: 'gaze_x', value: 'gaze_x' },
        { text: 'gaze_y', value: 'gaze_y'},
        { text: 'key', value: 'key' },
        { text: 'mouse_dx', value: 'mouse_dx' },
        { text: 'mouse_dy', value: 'mouse_dy' },
        { text: 'mouse_key', value: 'mouse_key'},
      ],
      options: {
        search: '',
        itemsPerPage: 10,
        page: 1,
        sortBy: [],
      },
      actions: [
        {"time": "2019-11-05 14:55:17.541782792",
          "gaze_x": 0.0,
          "gaze_y": 0.0,
          "key": {},
          "mouse_dx": 0.833,
          "mouse_dy": 0.167,
          "mouse_key": {}}
      ],
      loading: false,
      totalActions: 1,
      chartDataG: [
          ["time", "gaze_x", "gaze_y", "key", "mouse_dx", "mouse_dy", "mouse_key"],
          ["2019-11-05 14:55:17.541782792",0.0,0.0,{},1.0,0.0,{}],
          ["2019-11-05 14:55:17.548925649",0.0,0.0,{},0.667,0.0,{}],
          ["2019-11-05 14:55:17.556068506",0.0,0.0,{},1.6,0.0,{}],
          ["2019-11-05 14:55:17.563211363",0.0,0.0,{},0.75,0.0,{}],
          ["2019-11-05 14:55:17.570354220",0.0,0.0,{},1.0,0.0,{}],
          ["2019-11-05 14:55:17.577497077",0.0,0.0,{},0.833,0.167,{}],
          ["2019-11-05 14:55:17.584639934",0.0,0.0,{},1.0,0.0,{}],
          ["2019-11-05 14:55:17.591782791",0.0,0.0,{},0.75,0.0,{}],
          ["2019-11-05 14:55:17.598925648",0.0,0.0,{},0.667,0.167,{}],
          ["2019-11-05 14:55:17.606068505",0.0,0.0,{},0.833,0.0,{}],
          ["2019-11-05 14:55:17.613211362",0.0,0.0,{},0.5,0.0,{}],
          ["2019-11-05 14:55:17.620354219",0.0,0.0,{},0.8,0.0,{}],
          ["2019-11-05 14:55:17.627497076",0.0,0.0,{},0.5,-0.25,{}],
          ["2019-11-05 14:55:17.634639933",0.0,0.0,{},0.667,0.0,{}],
          ["2019-11-05 14:55:17.641782790",0.0,0.0,{},1.0,-0.333,{}],
          ["2019-11-05 14:55:17.648925647",0.0,0.0,{},1.0,-0.167,{}],
          ["2019-11-05 14:55:17.656068504",0.0,0.0,{},0.833,0.0,{}],
          ["2019-11-05 14:55:17.663211361",0.0,0.0,{},1.333,-0.333,{}],
          ["2019-11-05 14:55:17.670354218",0.0,0.0,{},0.833,0.0,{}],
          ["2019-11-05 14:55:17.677497075",0.0,0.0,{},0.667,-0.167,{}],
          ["2019-11-05 14:55:17.684639932",0.0,0.0,{},0.5,0.0,{}],
          ["2019-11-05 14:55:17.691782789",0.0,0.0,{},0.667,0.0,{}],
          ["2019-11-05 14:55:17.698925646",0.0,0.0,{},0.333,0.0,{}],
        ],
        charDataMouse: [
                    ["time", "mouse_dx", "mouse_dy", "mouse_key"], //"", "mouse_dy",
          ["2019-11-05 14:55:17.541782792",1.0,0.0,"['A','LCONTROL','A']"],
          ["2019-11-05 14:55:17.548925649",0.667,0.0,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.556068506",1.6,0.0,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.563211363",0.75,0.0,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.570354220",1.0,0.0,"['A','LCONTROL','LCONTROL']"],
          ["2019-11-05 14:55:17.577497077",0.833,0.167,"['A','A',]"],
          ["2019-11-05 14:55:17.584639934",1.0,0.0,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.591782791",0.75,0.0,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.598925648",0.667,0.167,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.606068505",0.833,0.0,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.613211362",0.5,0.0,"['A','A','LCONTROL']"],
          ["2019-11-05 14:55:17.620354219",0.8,0.0,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.627497076",0.5,-0.25,"['A','LCONTROL','LCONTROL']"],
          ["2019-11-05 14:55:17.634639933",0.667,0.0,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.641782790",1.0,-0.333,"['A','LCONTROL']"],
          ["2019-11-05 14:55:17.648925647",1.0,-0.167,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.656068504",0.833,0.0,"['A']"],
          ["2019-11-05 14:55:17.663211361",1.333,-0.333,"['LCONTROL']"],
          ["2019-11-05 14:55:17.670354218",0.833,0.0,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.677497075",0.667,-0.167,"['A','LCONTROL','A','LCONTROL']"],
          ["2019-11-05 14:55:17.684639932",0.5,0.0,"['LCONTROL']"],
          ["2019-11-05 14:55:17.691782789",0.667,0.0,"['A']"],
          ["2019-11-05 14:55:17.698925646",0.333,0.0,"['A']"],
        ],
        chartData: [
          ["ID", "X", "Y",],
          ["", 8.0, 1.67, ],
          ["", 7.9, 1.36, ],
          ["", 7.8, 1.84, ],
          ["", -7.2, 2.78, ],
          ["", 8.1, 2.00, ],
          ["", 7.2, -1.70, ],
          ["", 6.8, 4.77, ],
          ["", -8.2, 1.67, ],
          ["", -7.29, -1.36, ],
          ["", 7.33, 1.84, ],
          ["", 7.2, -2.78, ],
          ["", -5.1, 2.00, ],
          ["", -4.2, -1.70, ],
          ["", 7.8, 4.77, ]
        ],
        chartOptions: {
          width: 800,
          height: 500,
          title: 'Gamer Mouse Activity',
          sizeAxis: {minValue: 0,  maxSize: 5},
          legend: {position: 'top', textStyle: {color: 'blue', fontSize: 16}},
          explorer: {},
          hAxis: {title: 'mouse_dx'},
          vAxis: {title: 'mouse_dy'},
          colorAxis: { colors: ["yellow", "red"] },
        },
        chartEvents: {
          select: () => {
            console.log('event')
            const chart = this.$refs.mouseChart.chartObject;
            const selection = chart.getSelection();
            // handle event here
            if (selection) {
              if (this.notifications.length === 6) {
              this.notifications.shift();
              }
              this.notifications.push({'color': 'primary', 'text': `Выбрано действие ${this.chartDataG[selection[0]['row']]}.`});
              setTimeout(() => {
                this.notifications.shift();
              }, 3000);
            }
            //const onSelectionMeaasge = selection.length !== 0 ? `select data ${this.chartDataG[selection[0]['row']]}` : 'data was diselected';

            },
        },
    }
  },
  computed: {
    computedDateFormatted () {
      return this.formatDate(this.date)
    },
  },
  watch: {
    date () {
      this.dateFormatted = this.formatDate(this.date)
    },
  },
  methods: {
    formatDate (date) {
      if (!date) return null

      const [year, month, day] = date.split('-')
      return `${year}/${month}/${day}`
    },
    parseDate (date) {
      if (!date) return null

      const [year, month, day] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
  },
};
</script>
