import { Scheduler } from "./scheduler.module.js";

const terminalHideDelay = 300;
const terminalShowDelay = 100;

const scheduler = new Scheduler({
  appendTo: document.body,
  viewPreset: "hourAndDay",
  features: {
    dependencies: {
      clickWidth: 5,
      radius: 10,
      terminalOffset: 0,
      terminalSize: 12,
      terminalShowDelay,
      terminalHideDelay,
    },
    dependencyEdit: {
      showLagField: false,
    },
  },
  crudManager: {
    loadUrl: "/load",
    autoLoad: true,
    syncUrl: "/sync",
    autoSync: true,
    // This config enables response validation and dumping of found errors to the browser console.
    // It's meant to be used as a development stage helper only so please set it to false for production systems.
    validateResponse: true,
  },
  columns: [{ text: "Name", field: "name", width: 130 }],
});