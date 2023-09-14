
import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self,root):
         self.root = root
         self.root.title("To_do list App")
         self.task_entry = tk.Entry(self.root)
         self.task_entry.pack(pady=10)

         self.task_listbox = tk.Listbox(root)
         self.task_listbox.pack()

         self.add_button = tk.Button(self.root, text="Add Task", command= self.add_task)
         self.add_button.pack()

         self.delete_button = tk.Button(self.root, text="Remove Task", command= self.delete_task)
         self.delete_button.pack()

         self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
         self.update_button.pack()
         
         self.tasks = ["Task 1", "Task 2", "Task 3"]
         self.refresh_task_list()


    def add_task(self):

        try:
              task = self.task_entry.get()
              if task:
                self.task_listbox.insert(tk.END,task)
                self.task_entry.delete(0,tk.END)
              #else:
                #messagebox.showwarning("Warning","Please enter the task")
              
        except Exception as e:
              print("Error occured: {e}")

        

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                selected_task_index = selected_task_index[0]
                self.tasks[selected_task_index] = new_task
                self.refresh_task_list()
                self.task_entry.delete(0, tk.END)
    
         
    def delete_task(self):
          selected_task_index = self.task_listbox.curselection()
          if selected_task_index:
              self.task_listbox.delete(selected_task_index)
          else:
              messagebox.showwarning("Warning", "Please select a task to remove")
         
         
def main():
        root = tk.Tk()
        app = TodoListApp(root)
        
        root.mainloop()

    

if __name__ == "__main__":
    main()

