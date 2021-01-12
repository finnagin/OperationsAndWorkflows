# About
This document will catalogue the various design decisions that need to be made/were made in the process of creating the operations and workflow language.

# Current design questions

1. Operate on multiple messages
    1. URI/URL or
    1. POSTing the message itself or
    1. Both
1. Communications of operations
    1. Generic endpoint, upload, designate what operation you want to perform. 
1. How do you return operations that were actually done
    1. Proposal: “processing_actions_executed”
1. Should operations language work across all platforms
    1. Leaning towards no: a “courier” would take a TRAPI QG + processing actions, identify which ARA’s can do what, and handle the hand-off of messages and return answers to the ARS.
1. What is the topology / control structure of a workflow?
    1. Linear?
    1. Branched/joined? (i.e. a DAG)
    1. Conditionals?
