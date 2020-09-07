<template>
    <v-container>
        <DateTimePicker
        ></DateTimePicker>
        <v-row justify="center">
        <Charts
          :charDataGazeProp="charDataGazeProp"
          :charDataMouseProp="charDataMouseProp"
        ></Charts>
        <DataTable
          :table_data="table_data"
          :total="total"
          :page="page"
          @tabelActions="refreshTable"
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
          table_data: null,
          pages: null,
          total: 0,
          charDataGazeProp: [],
          charDataMouseProp: [],
      }
  },
  components: { DateTimePicker, Charts, DataTable
  },
  mounted () {
    this.getActions()
  },
  methods: {
      getActions() {
            axios.get('/', {
                params: {
                    per_page: this.per_page,
                    //search: this.options.search,
                    //ordering: this.ordering,
                    page: this.page,
                }
            }).then((response) => {
                      if (response.status === 200) {
                          console.log(response.data);
                          this.table_data = response.data.actions;
                          this.total = response.data.total;
                          this.pages = response.data.pages;
                          let gaze = [];
                          let mouse = [];
                          // let key = '';
                          // let mouse_key = '';
                          response.data.actions.forEach(e => {
                              gaze.push([e.time.toString(), e.gaze_x, e.gaze_y, JSON.stringify(e.keys)]);
                              mouse.push([e.time.toString(), e.mouse_dx, e.mouse_dy, JSON.stringify(e.mouse_keys)]);
                          });
                          this.charDataGazeProp = gaze;
                          this.charDataMouseProp = mouse;
                          console.log(gaze);
                      }
                      else {
                          console.log(`error response ${response.status}`)
                      }
            })
      },
      refreshTable(page, per_page) {
          console.log('refresh')
          this.page = page;
          this.per_page = per_page;
          this.getActions();
      }
  }
}
</script>
