<template>
     <v-row align="start" justify="center">
      <v-col cols="1">
        <v-menu
          ref="startDateMenu"
          v-model="startDateMenu"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="startDate"
              label="Start Date"
              hint="Start Date"
              persistent-hint
              prepend-icon="mdi-calendar-month-outline"
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker v-model="startDate" no-title @input="startDateMenu = false"></v-date-picker>
        </v-menu>
      </v-col>
      <v-col cols="1">
      <v-menu
        ref="startTimeMenu"
        v-model="startTimeMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="startTime"
        transition="scale-transition"
        offset-y
        max-width="290px"
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="startTime"
            label="Select Start Time"
            prepend-icon="mdi-clock-outline"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-time-picker
          v-if="startTimeMenu"
          v-model="startTime"
          full-width
          format="24hr"
          use-seconds
          @click:second="$refs.startTimeMenu.save(startTime)"
        ></v-time-picker>
      </v-menu>
      </v-col>

      <v-col cols="1">
        <v-menu
          v-model="endDateMenu"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="endDate"
              label="End Date"
              hint="End Date"
              persistent-hint
              prepend-icon="mdi-calendar-month-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker v-model="endDate" no-title @input="endDateMenu = false"></v-date-picker>
        </v-menu>
      </v-col>

      <v-col cols="1">
      <v-menu
        ref="endTimeMenu"
        v-model="endTimeMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="endTime"
        transition="scale-transition"
        offset-y
        max-width="290px"
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="endTime"
            label="Select End Time"
            prepend-icon="mdi-clock-outline"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-time-picker
          v-if="endTimeMenu"
          v-model="endTime"
          full-width
          format="24hr"
          use-seconds
          @click:second="$refs.endTimeMenu.save(endTime)"
        ></v-time-picker>
      </v-menu>
      </v-col>

     </v-row>
</template>

<script>
    export default {
        name: "DateTimePicker",
        data() {
            return {
                startDate: new Date('2019-11-05').toISOString().substr(0, 10),
                endDate: new Date('2020-11-05').toISOString().substr(0, 10),
                startDateMenu: false,
                endDateMenu: false,
                startTime: '14:55:17',
                endTime: '14:56:37',
                startTimeMenu: false,
                endTimeMenu: false
            }
        }

    }
</script>

<style scoped>

</style>