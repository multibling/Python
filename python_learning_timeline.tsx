import React, { useState } from 'react';
import { ChevronDown, ChevronUp, CheckCircle2, Circle } from 'lucide-react';

export default function PythonTimeline() {
  const [expandedMonth, setExpandedMonth] = useState(0);
  const [completedTasks, setCompletedTasks] = useState({});

  const timeline = [
    {
      month: "Month 1: Python Basics",
      weeks: "Weeks 1-4",
      hoursPerWeek: 7,
      milestones: [
        "Understand variables, data types, and basic operations",
        "Learn conditional statements (if/elif/else)",
        "Master loops (for, while)"
      ],
      assignments: [
        "Assignment 1.1: Create a simple number guessing game",
        "Assignment 1.2: Build a program that calculates BMI based on user input",
        "Assignment 1.3: Write a program using loops to print multiplication tables"
      ],
      recap: "Recap: Write a program combining variables, conditionals, and loops (e.g., a password validator)"
    },
    {
      month: "Month 2: Functions & Data Structures",
      weeks: "Weeks 5-8",
      hoursPerWeek: 7,
      milestones: [
        "Master function definition and parameters",
        "Learn lists, tuples, and dictionaries",
        "Understand list comprehensions and dictionary operations"
      ],
      assignments: [
        "Assignment 2.1: Create functions for common mathematical operations",
        "Assignment 2.2: Build a simple contact book using dictionaries",
        "Assignment 2.3: Work with lists—filter, sort, and manipulate data"
      ],
      recap: "Recap: Build a mini project combining functions and data structures (e.g., a grade calculator)"
    },
    {
      month: "Month 3: File Handling & Debugging",
      weeks: "Weeks 9-12",
      hoursPerWeek: 7,
      milestones: [
        "Learn file I/O operations (read, write, append)",
        "Understand exception handling (try/except)",
        "Practice debugging techniques"
      ],
      assignments: [
        "Assignment 3.1: Create a program that reads and writes to a text file",
        "Assignment 3.2: Build a to-do list app that saves to a file",
        "Assignment 3.3: Write error-handling code for user input validation"
      ],
      recap: "Recap: Build a journaling app that saves entries to files with proper error handling"
    },
    {
      month: "Month 4: Object-Oriented Programming",
      weeks: "Weeks 13-16",
      hoursPerWeek: 7,
      milestones: [
        "Understand classes and objects",
        "Learn inheritance and polymorphism",
        "Master encapsulation and attributes"
      ],
      assignments: [
        "Assignment 4.1: Create a class for a simple game character with attributes and methods",
        "Assignment 4.2: Build a bank account system with parent/child classes",
        "Assignment 4.3: Design a pet adoption system using OOP principles"
      ],
      recap: "Recap: Build a small game or application using multiple classes (e.g., a simple inventory system)"
    },
    {
      month: "Month 5: Capstone & Beyond",
      weeks: "Weeks 17-20",
      hoursPerWeek: 7,
      milestones: [
        "Review all concepts learned",
        "Explore libraries (requests, json, datetime)",
        "Build and polish a capstone project"
      ],
      assignments: [
        "Assignment 5.1: Create a program that fetches data from an API using requests library",
        "Assignment 5.2: Build a data analysis tool using JSON files",
        "Assignment 5.3: Capstone—build a complete project using everything learned"
      ],
      recap: "Recap: Complete your capstone project and document it. Suggestions: weather app, expense tracker, or book cataloging system"
    }
  ];

  const toggleMonth = (index) => {
    setExpandedMonth(expandedMonth === index ? -1 : index);
  };

  const toggleTask = (taskId) => {
    setCompletedTasks(prev => ({
      ...prev,
      [taskId]: !prev[taskId]
    }));
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-3xl mx-auto">
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-indigo-900 mb-2">🐍 Python Learning Timeline</h1>
          <p className="text-indigo-700">5 Months • 7 Hours/Week • 140 Total Hours</p>
          <p className="text-sm text-indigo-600 mt-2">Based on Python Crash Course curriculum</p>
        </div>

        <div className="space-y-4">
          {timeline.map((phase, idx) => (
            <div key={idx} className="bg-white rounded-lg shadow-md overflow-hidden">
              <button
                onClick={() => toggleMonth(idx)}
                className="w-full p-5 flex items-center justify-between hover:bg-indigo-50 transition-colors"
              >
                <div className="text-left">
                  <h2 className="text-xl font-bold text-indigo-900">{phase.month}</h2>
                  <p className="text-sm text-indigo-600">{phase.weeks} • {phase.hoursPerWeek} hrs/week</p>
                </div>
                {expandedMonth === idx ? (
                  <ChevronUp className="text-indigo-600" size={24} />
                ) : (
                  <ChevronDown className="text-indigo-600" size={24} />
                )}
              </button>

              {expandedMonth === idx && (
                <div className="px-5 pb-5 border-t border-indigo-100">
                  <div className="mt-5">
                    <h3 className="font-semibold text-indigo-900 mb-3">📍 Milestones</h3>
                    <ul className="space-y-2 ml-4 mb-5">
                      {phase.milestones.map((milestone, mIdx) => (
                        <li key={mIdx} className="text-indigo-700 flex items-start">
                          <span className="mr-2">✓</span>
                          {milestone}
                        </li>
                      ))}
                    </ul>
                  </div>

                  <div className="mt-5">
                    <h3 className="font-semibold text-indigo-900 mb-3">📝 Assignments</h3>
                    <div className="space-y-2 mb-5">
                      {phase.assignments.map((assignment, aIdx) => {
                        const taskId = `${idx}-${aIdx}`;
                        return (
                          <button
                            key={aIdx}
                            onClick={() => toggleTask(taskId)}
                            className="w-full text-left p-3 bg-indigo-50 rounded-lg hover:bg-indigo-100 transition-colors flex items-start"
                          >
                            {completedTasks[taskId] ? (
                              <CheckCircle2 className="text-green-500 mr-3 mt-0.5 flex-shrink-0" size={20} />
                            ) : (
                              <Circle className="text-indigo-400 mr-3 mt-0.5 flex-shrink-0" size={20} />
                            )}
                            <span className={completedTasks[taskId] ? "line-through text-indigo-500" : "text-indigo-900"}>
                              {assignment}
                            </span>
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  <div className="mt-5 p-3 bg-yellow-50 border-l-4 border-yellow-400 rounded">
                    <h3 className="font-semibold text-yellow-900 mb-2">🎯 Recap Challenge</h3>
                    <p className="text-yellow-800 text-sm">{phase.recap}</p>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>

        <div className="mt-8 bg-indigo-900 text-white p-5 rounded-lg">
          <h3 className="font-bold mb-3">💡 Tips for Success</h3>
          <ul className="text-sm space-y-2">
            <li>• Code daily when possible, even if for 30 minutes</li>
            <li>• Don't just watch tutorials—type code yourself</li>
            <li>• Reference official Python docs at python.org/docs</li>
            <li>• On days you can't code, review past assignments or take notes</li>
            <li>• Join Python communities (Reddit, Discord) for help and motivation</li>
          </ul>
        </div>
      </div>
    </div>
  );
}