/*
  ProgramIdentifier

d{a}[:{b}] where 0 < a < 6 and 0 < b < 9

d1 = monday
d5 = friday
etc

d1:8 - monday, 8th period

*/

const Schemas = {
  Teacher: {
    name: String,
    subject: String,
    unavailability: ["String,ProgramIdentifier"],
    id: "String,Unique",
  },
  Class: {
    subjects: ["String:Teacher.id"]
  }
}

console.log("UwU");