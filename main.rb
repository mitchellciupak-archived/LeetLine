#Created by: Mitchell Ciupak
#Date: 20200610

# Imports
require "Thor"
require "PStore"

class TODOApp < Thor
    desc "add_task NAME", "ask a new task to your TODO"

    def add_task(name)
        PStore.new("/tmp/task.txt").transation { |store| store[name] = true}
    end

    desc "list_task", "list all tasks on your TODO"

    def list_task(name)
        PStore.new("/tmp/task.txt").transation do |store|
            store.roots.each_with_index { |task,idx| puts"#{idx+1}.#{task}"}
        end
    end
end


TODOApp.start(ARGV)