#Created by: Mitchell Ciupak
#Date: 20200610

# Imports
require "Thor"
require "PStore"

class LeetLine < Thor
    ## Constuctor to Show List of Options

    ## Features
    ### Add
    #### Breaks into Item class 
    ### Remove
    #### Params: ID
    ### List
    #### Params: All(Default), Recent(Top 15), Longest(Top 15)
    ### Select
    #### Params: Random(Default), ID, String

    # ADD
    ## Desciption
    desc "add NAME", "Add Question and Anwser to Library"
    ## Definition
    def add(name)
        PStore.new("/tmp/task.txt").transation { |store| store[name] = true}
    end

    
    desc "list", "list all tasks on your TODO"

    def list(name)
        PStore.new("/tmp/task.txt").transation do |store|
            store.roots.each_with_index { |task,idx| puts"#{idx+1}.#{task}"}
        end
    end


end


LeetLine.start(ARGV)