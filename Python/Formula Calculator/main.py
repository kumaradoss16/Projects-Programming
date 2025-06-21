import tkinter as tk
import math
from tkinter.font import Font

root = tk.Tk()
# Icon image file
icon = tk.PhotoImage(file="img.png")
# setting icon of root window
root.iconphoto(False, icon)
root.geometry("800x800")
root.resizable(height=False, width=False)
root.title("Formula Calculator")
font1 = Font(size=15, weight="bold")
entry = tk.Entry(root)


# Popup window for Mechanics page formula
# Create Popup window for Velocity
def popup():
    popup_window = tk.Toplevel(root, bg="#444654")
    popup_window.title("Calculator")
    popup_window.geometry("620x600")
    popup_window.resizable(height=False, width=False)
    # Create Velocity layout
    # Create label for Velocity
    label1 = tk.Label(popup_window, text="Velocity", font=("Calbiri", 17, "bold"), padx=250, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for displacement and time.
    displacement_label = tk.Label(popup_window, text="Distance (m): ", font=("Terakatal", 14), bg="#444654")
    displacement_label.grid(row=1, column=0)
    displacement_entry = tk.Entry(popup_window, width=15, font="sans-serif")
    displacement_entry.grid(row=1, column=1, padx=5, pady=5)

    time_label = tk.Label(popup_window, text="Time (s): ", font=("Terakatal", 14), bg="#444654")
    time_label.grid(row=2, column=0)
    time_entry = tk.Entry(popup_window, width=15, font="sans-serif")
    time_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a button to calculate velocity and clear.
    calculate_button = tk.Button(popup_window, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_velocity(displacement_entry, time_entry, velocity_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    # Create a label to display the velocity.
    velocity_label = tk.Label(popup_window, bg="#444654", fg="#0002a1", font=("Verdana", 14))
    velocity_label.grid(row=4, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear(displacement_entry, time_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)
    # Definition
    lab = tk.Label(popup_window, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window, height=4, width=69, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = ("""VELOCITY:   
              Velocity is a physical quantity that describes the rate at which an object 
changes its position with respect to time. It is a vector quantity, meaning it has 
both magnitude and direction.""")
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window, width=69, height=7, font=("Terakatal", 12), bg="grey")
    For1 = """The formula for acceleration is:
       v = Δx / Δt
       
    where:
       v = Velocity
      Δx = displacement of the object in a given direction
      Δt = is the time taken for that displacement to occur."""
    T2.grid(row=9, column=0, columnspan=5, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window.mainloop()


# Create Popup window for Acceleration
def popup1():
    popup_window1 = tk.Toplevel(root, bg="#444654")
    popup_window1.title("Calculator")
    popup_window1.geometry("610x580")
    popup_window1.resizable(height=False, width=False)
    # Create acceleration layout
    # Create label for Acceleration
    label1 = tk.Label(popup_window1, text="Acceleration", font=("Calbiri", 17, "bold"), padx=210, pady=5, fg="#3A98B9",
                      bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for initial velocity, final velocity, and time.
    initial_velocity_label = tk.Label(popup_window1, text="Initial Velocity (m/s): ", font=("Terakatal", 14),
                                      bg="#444654")
    initial_velocity_label.grid(row=1, column=0)
    initial_velocity_entry = tk.Entry(popup_window1, width=15, font="sans-serif")
    initial_velocity_entry.grid(row=1, column=1, padx=5, pady=5)

    final_velocity_label = tk.Label(popup_window1, text="Final Velocity (m/s): ", font=("Terakatal", 14), bg="#444654")
    final_velocity_label.grid(row=2, column=0)
    final_velocity_entry = tk.Entry(popup_window1, width=15, font="sans-serif")
    final_velocity_entry.grid(row=2, column=1, padx=5, pady=5)

    time1_label = tk.Label(popup_window1, text="Time (s): ", font=("Terakatal", 14), bg="#444654")
    time1_label.grid(row=3, column=0)
    time_entry = tk.Entry(popup_window1, width=15, font="sans-serif")
    time_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a button to calculate acceleration and clear.
    calculate_button = tk.Button(popup_window1, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_acceleration(initial_velocity_entry, final_velocity_entry,
                                                                        time_entry, acceleration_label))
    calculate_button.grid(row=4, column=1, padx=5, pady=5)

    # Create a label to display the acceleration.
    acceleration_label = tk.Label(popup_window1, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    acceleration_label.grid(row=5, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window1, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear1(initial_velocity_entry, final_velocity_entry, time_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window1, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window1, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, column=0, columnspan=2)

    T = tk.Text(popup_window1, height=3, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """ACCELERATION:
             Acceleration is a measure of how quickly an object changes its velocity 
over time. It is a vector quantity, meaning it has both magnitude and direction."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window1, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=9, column=0, columnspan=2)

    T2 = tk.Text(popup_window1, height=6, width=69, font=("Terakatal", 12), bg="grey")
    For1 = """The formula for acceleration is:
       a = Δv / Δt
       
    where:    
      Δv = difference between the final velocity and the initial velocity of the object.
      Δt = time taken for that change in velocity to occur."""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window1.mainloop()


# Create Popup window for Equation of Motion
def popup2():
    popup_window2 = tk.Toplevel(root, bg="#444654")
    popup_window2.title("Calculator")
    popup_window2.geometry("620x630")
    popup_window2.resizable(height=False, width=False)
    # Create Equation of motion layout
    # Create label for Equation of Motion
    label1 = tk.Label(popup_window2, text="Equation of Motion", font=font1, padx=200, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for acceleration, initial velocity and time.
    acceleration1_label = tk.Label(popup_window2, text="Acceleration (m/s²): ", font=("Terakatal", 14), bg="#444654")
    acceleration1_label.grid(row=1, column=0, padx=5, pady=5)
    acceleration1_entry = tk.Entry(popup_window2, width=15, font="sans-serif")
    acceleration1_entry.grid(row=1, column=1, padx=5, pady=5)

    initial_velocity1_label = tk.Label(popup_window2, text="Initial Velocity (m/s): ", font=("Terakatal", 14),
                                       bg="#444654")
    initial_velocity1_label.grid(row=2, column=0, padx=5, pady=5)
    initial_velocity1_entry = tk.Entry(popup_window2, width=15, font="sans-serif")
    initial_velocity1_entry.grid(row=2, column=1, padx=5, pady=5)

    time2_label = tk.Label(popup_window2, text="Time (s): ", font=("Terakatal", 14), bg="#444654")
    time2_label.grid(row=3, column=0, padx=5, pady=5)
    time2_entry = tk.Entry(popup_window2, width=15, font="sans-serif")
    time2_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window2, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_equation_of_motion(acceleration1_entry, time2_entry,
                                                                              initial_velocity1_entry, velocity1_label))
    calculate_button.grid(row=4, column=1, padx=5, pady=5)

    # Create a label to display the velocity1(equation of motion).
    velocity1_label = tk.Label(popup_window2, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    velocity1_label.grid(row=5, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window2, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear2(initial_velocity1_entry, acceleration1_entry, time2_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)
    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window2, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)
    # Definition
    lab = tk.Label(popup_window2, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window2, height=4, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """EQUATION OF MOTION:
                  The equation of motion refers to a mathematical relationship that 
describes the motion of an object in terms of its position, velocity, and 
acceleration with respect to time. """
    T.grid(row=8, column=0, columnspan=4, sticky="w")
    # Insert the Definition
    T.insert(tk.END, Def)
    # Formula
    lab = tk.Label(popup_window2, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window2, height=7, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    For1 = """The formula for acceleration is:
       v = a.t + u
       
    where:
       v = Velocity
       a = Acceleration
       t = Time
       u = initial velocity"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window2.mainloop()


# Create Popup window for Force
def popup3():
    popup_window3 = tk.Toplevel(root, bg="#444654")
    popup_window3.title("Calculator")
    popup_window3.geometry("620x590")
    popup_window3.resizable(height=False, width=False)
    # Create Force layout
    # Create a label for force.
    label1 = tk.Label(popup_window3, text="Force", font=font1, padx=270, pady=5, fg="#3A98B9", bd=1, borderwidth=2,
                      relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Mass and Acceleration.
    mass_label = tk.Label(popup_window3, text="Mass (kg): ", font=("Terakatal", 14), bg="#444654")
    mass_label.grid(row=1, column=0)
    mass_entry = tk.Entry(popup_window3, width=15, font="sans-serif")
    mass_entry.grid(row=1, column=1, padx=5, pady=5)

    acceleration2_label = tk.Label(popup_window3, text="Acceleration (m/s²): ", font=("Terakatal", 14), bg="#444654")
    acceleration2_label.grid(row=2, column=0)
    acceleration2_entry = tk.Entry(popup_window3, width=15, font="sans-serif")
    acceleration2_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window3, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_force(mass_entry, acceleration2_entry, force_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window3, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear3(mass_entry, acceleration2_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Force.
    force_label = tk.Label(popup_window3, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    force_label.grid(row=4, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window3, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window3, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window3, height=4, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """FORCE:
             A force is any interaction that, when unopposed, will change the motion 
of an object. A force can cause an object with mass to change its velocity. Force 
can also be described intuitively as a push or a pull."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)
    # Formula
    lab = tk.Label(popup_window3, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window3, height=7, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    For1 = """The formula for Force is:
       F = m.a
       
    where:
       F = Force
       m = Mass
       a = Acceleration"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window3.mainloop()


# Create Popup window for Centripetal Acceleration
def popup4():
    popup_window4 = tk.Toplevel(root, bg="#444654")
    popup_window4.title("Calculator")
    popup_window4.geometry("620x630")
    popup_window4.resizable(height=False, width=False)
    # Create a Centripetal Acceleration layout.
    # Create a label for Centripetal Acceleration.
    label1 = tk.Label(popup_window4, text="Centripetal Acceleration", font=font1, padx=180, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Linear Velocity and Radius.
    linear_velocity_label = tk.Label(popup_window4, text="Linear velocity (m/s): ", font=("Terakatal", 14),
                                     bg="#444654")
    linear_velocity_label.grid(row=1, column=0, )
    linear_velocity_entry = tk.Entry(popup_window4, width=15, font="sans-serif")
    linear_velocity_entry.grid(row=1, column=1, padx=5, pady=5)

    radius_label = tk.Label(popup_window4, text="Radius (m): ", font=("Terakatal", 14), bg="#444654")
    radius_label.grid(row=2, column=0)
    radius_entry = tk.Entry(popup_window4, width=15, font="sans-serif")
    radius_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window4, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_centripetal_acceleration(linear_velocity_entry, radius_entry,
                                                                                    centripetal_acceleration_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    # Create a label to display the Centripetal Acceleration.
    centripetal_acceleration_label = tk.Label(popup_window4, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    centripetal_acceleration_label.grid(row=4, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window4, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear4(linear_velocity_entry, radius_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)
    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window4, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)
    # Definition
    lab = tk.Label(popup_window4, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window4, height=6, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """CENTRIPETAL ACCELERATION:
                Centripetal acceleration is the acceleration experienced by an object 
moving in a circular path, directed towards the center of the circle or the axis of rotation It is always perpendicular to the object's velocity and is responsible for continuously changing the direction of the object's motion, keeping it in a curved path."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")
    # Insert the Definition
    T.insert(tk.END, Def)
    # Formula
    lab = tk.Label(popup_window4, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window4, height=6, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    For1 = """The formula for Centripetal Acceleration is:
       a = v²/r
       
    where:
       a = Acceleration
       v = Linear Velocity
       r = Radius"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window4.mainloop()


# Create Popup window for Momentum
def popup5():
    popup_window5 = tk.Toplevel(root, bg="#444654")
    popup_window5.title("Calculator")
    popup_window5.geometry("635x600")
    popup_window5.resizable(height=False, width=False)
    # Create a Momentum layout
    # Create a label for Momentum.
    label1 = tk.Label(popup_window5, text="MOMENTUM", font=font1, padx=247, pady=5, fg="#3A98B9", bd=1, borderwidth=2,
                      relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for mass and velocity.
    mass_label = tk.Label(popup_window5, text="Mass (kg): ", font=("Terakatal", 14), bg="#444654")
    mass_label.grid(row=1, column=0)
    mass_entry = tk.Entry(popup_window5, width=15, font="sans-serif")
    mass_entry.grid(row=1, column=1, padx=5, pady=5)

    velocity_label = tk.Label(popup_window5, text="Velocity (m/s): ", font=("Terakatal", 14), bg="#444654")
    velocity_label.grid(row=2, column=0)
    velocity_entry = tk.Entry(popup_window5, width=15, font="sans-serif")
    velocity_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window5, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_momentum(mass_entry, velocity_entry, momentum_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    # Create a label to display the Momentum.
    momentum_label = tk.Label(popup_window5, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    momentum_label.grid(row=4, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window5, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear5(mass_entry, velocity_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window5, width=630, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window5, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window5, height=5, width=70, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """MOMENTUM:
             Momentum is a fundamental property of a moving object that describes its 
motion and resistance to change in motion. It is defined as the product of an 
object's mass and velocity, and is a vector quantity, meaning it has both magnitude and direction."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")
    # Insert the Definition
    T.insert(tk.END, Def)
    # Formula
    lab = tk.Label(popup_window5, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window5, height=6, width=70, font=("Terakatal", 12), bg="grey", borderwidth=1)
    For1 = """The formula for Momentum is:
       p = m.v
       
    where:
       p = Momentum
       m = Mass
       v = Velocity"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window5.mainloop()


# Create Popup window for Impulse
def popup6():
    popup_window6 = tk.Toplevel(root, bg="#444654")
    popup_window6.title("Calculator")
    popup_window6.geometry("620x600")
    popup_window6.resizable(height=False, width=False)
    # Create a Impulse layout
    # Create a label for Impulse.
    label1 = tk.Label(popup_window6, text="IMPULSE", font=font1, padx=260, pady=5, fg="#3A98B9", bd=1, borderwidth=2,
                      relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Force and Time change.
    force_label = tk.Label(popup_window6, text="Force (N): ", font=("Terakatal", 14), bg="#444654")
    force_label.grid(row=1, column=0)
    force_entry = tk.Entry(popup_window6, width=15, font="sans-serif")
    force_entry.grid(row=1, column=1, padx=5, pady=5)

    time_change_label = tk.Label(popup_window6, text="Time Chane (s):", font=("Terakatal", 14), bg="#444654")
    time_change_label.grid(row=2, column=0)
    time_change_entry = tk.Entry(popup_window6, width=15, font="sans-serif")
    time_change_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window6, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_impulse(force_entry, time_change_entry, impulse_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window6, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear6(force_entry, time_change_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Impulse.
    impulse_label = tk.Label(popup_window6, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    impulse_label.grid(row=4, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window6, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window6, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window6, height=4, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """IMPULSE:
               Impulse is a quantity that measures the change in momentum of an 
object resulting from an applied force. It is a vector quantity, meaning it has 
both magnitude and direction."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window6, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window6, height=6, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    For1 = """The formula for Impulse is:
       I = F.Δt
where:
       I = Impulse
       F = Force
      Δt = Time change"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window6.mainloop()


# Create Popup window for Work
def popup7():
    popup_window7 = tk.Toplevel(root, bg="#444654")
    popup_window7.title("Calculator")
    popup_window7.geometry("620x600")
    popup_window7.resizable(height=False, width=False)
    # Create a Work layout
    # Create a label for Work.
    label1 = tk.Label(popup_window7, text="WORK", font=font1, padx=272, pady=5, fg="#3A98B9", bd=1, borderwidth=2,
                      relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Force and Displacement
    force_label = tk.Label(popup_window7, text="Force (N): ", font=("Terakatal", 14), bg="#444654")
    force_label.grid(row=1, column=0)
    force_entry = tk.Entry(popup_window7, width=15, font="sans-serif")
    force_entry.grid(row=1, column=1, padx=5, pady=5)

    displacement_label = tk.Label(popup_window7, text="Displacement (m):", font=("Terakatal", 14), bg="#444654")
    displacement_label.grid(row=2, column=0)
    displacement_entry = tk.Entry(popup_window7, width=15, font="sans-serif")
    displacement_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate Work and clear button.
    calculate_button = tk.Button(popup_window7, text="Calculate", borderwidth=2, font=("Terakatal", 14),
                                 command=lambda: calculate_work(force_entry, displacement_entry, work_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window7, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear7(force_entry, displacement_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Work.
    work_label = tk.Label(popup_window7, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    work_label.grid(row=4, column=1, padx=5, pady=5)
    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window7, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)
    # Definition
    lab = tk.Label(popup_window7, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window7, height=4, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """WORK:
             Work is defined as the product of the force applied to an object and the 
distance over which that force is applied. It is a scalar quantity, meaning it has 
magnitude but no direction."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")
    # Insert the Definition
    T.insert(tk.END, Def)
    # Formula
    lab = tk.Label(popup_window7, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window7, height=7, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    For1 = """The formula for Work is:
       W = F . s 
       
    where:
       W = Work
       F = Force
       s = Displacement"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window7.mainloop()


# Create Popup window for Kinetic energy
def popup8():
    popup_window8 = tk.Toplevel(root, bg="#444654")
    popup_window8.title("Calculator")
    popup_window8.geometry("620x600")
    popup_window8.resizable(height=False, width=False)
    # Create a kinetic energy layout
    # Create a label for Kinetic energy.
    label1 = tk.Label(popup_window8, text="Kinetic energy", font=font1, padx=230, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for displacement and time.
    mass_label = tk.Label(popup_window8, text="Mass (kg): ", font=("Terakatal", 14), bg="#444654")
    mass_label.grid(row=1, column=0)
    mass_entry = tk.Entry(popup_window8, width=15, font="sans-serif")
    mass_entry.grid(row=1, column=1, padx=5, pady=5)

    speed_label = tk.Label(popup_window8, text="Speed (m/s):", font=("Terakatal", 14), bg="#444654")
    speed_label.grid(row=2, column=0)
    speed_entry = tk.Entry(popup_window8, width=15, font="sans-serif")
    speed_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window8, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_kinetic_energy(mass_entry, speed_entry,
                                                                          kinetic_energy_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window8, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear8(mass_entry, speed_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Kinetic Energy.
    kinetic_energy_label = tk.Label(popup_window8, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    kinetic_energy_label.grid(row=4, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window8, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window8, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window8, height=3, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """KINETIC ENERGY:
             Kinetic energy is a form of energy associated with the motion of an object. It is the energy that an object possesses due to its velocity or movement."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window8, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window8, height=7, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    For1 = """The formula for Kinetic Energy is:
     K.E = 1/2.m.v²
     
     where:
     K.E = Kinetic Energy
       m = Mass
       v = Speed"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window8.mainloop()


# Create Popup window for Potential energy
def popup9():
    popup_window9 = tk.Toplevel(root, bg="#444654")
    popup_window9.title("Calculator")
    popup_window9.geometry("620x580")
    popup_window9.resizable(height=False, width=False)
    # Create a Potential energy layout
    # Create a label for Potential energy.
    label1 = tk.Label(popup_window9, text="Potential energy", font=font1, padx=220, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for mass and height.
    mass_label = tk.Label(popup_window9, text="Mass (kg): ", font=("Terakatal", 14), bg="#444654")
    mass_label.grid(row=1, column=0)
    mass_entry = tk.Entry(popup_window9, width=15, font="sans-serif")
    mass_entry.grid(row=1, column=1, padx=5, pady=5)

    height_label = tk.Label(popup_window9, text="Height (m):", font=("Terakatal", 14), bg="#444654")
    height_label.grid(row=2, column=0, padx=5, pady=5)
    height_entry = tk.Entry(popup_window9, width=15, font="sans-serif")
    height_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window9, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_potential_energy(mass_entry, height_entry,
                                                                            potential_energy_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window9, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear9(mass_entry, height_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Potential energy.
    potential_energy_label = tk.Label(popup_window9, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    potential_energy_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window9, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window9, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window9, height=3, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """POTENTIAL ENERGY:
             Potential energy can be defined as the energy stored in an object due to 
the object’s relative position in a system with other objects."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window9, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window9, height=7, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    For1 = """The formula for Potential Energy is:
       U = m.g.h

    where:
       U = Potential Energy
       m = Mass
       h = Height"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window9.mainloop()


# Create Popup window for Efficiency
def popup10():
    popup_window10 = tk.Toplevel(root, bg="#444654")
    popup_window10.title("Calculator")
    popup_window10.geometry("620x590")
    popup_window10.resizable(height=False, width=False)
    # Create Efficiency layout
    # Create label for Efficiency.
    label1 = tk.Label(popup_window10, text="Efficiency", font=font1, padx=250, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for net power output and heat flow rate.
    net_power_output_label = tk.Label(popup_window10, text="Net power output (J/s): ", font=("Terakatal", 14),
                                      bg="#444654")
    net_power_output_label.grid(row=1, column=0)
    net_power_output_entry = tk.Entry(popup_window10, width=15, font="sans-serif")
    net_power_output_entry.grid(row=1, column=1, padx=5, pady=5)

    heat_flow_rate_label = tk.Label(popup_window10, text="Heat flow rate(J/s):", font=("Terakatal", 14), bg="#444654")
    heat_flow_rate_label.grid(row=2, column=0)
    heat_flow_rate_entry = tk.Entry(popup_window10, width=15, font="sans-serif")
    heat_flow_rate_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window10, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_efficiency(net_power_output_entry, heat_flow_rate_entry,
                                                                      efficiency_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window10, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear10(net_power_output_entry, heat_flow_rate_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Efficiency.
    efficiency_label = tk.Label(popup_window10, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    efficiency_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window10, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window10, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window10, height=3, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """EFFICIENCY:
    Efficiency is the ratio of the work performed by a machine or in a process to 
the total energy expended or heat consumed."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window10, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window10, height=7, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    For1 = """The formula for Efficiency is:
       n = W / Q
 
    where:
       n = Efficiency
       W = Net power output
       Q = Heat flow rate"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window10.mainloop()


# Create Popup window for Power
def popup11():
    popup_window11 = tk.Toplevel(root, bg="#444654")
    popup_window11.title("Calculator")
    popup_window11.geometry("620x590")
    popup_window11.resizable(height=False, width=False)
    # Create a Power layout
    # Create a label for Power.
    label1 = tk.Label(popup_window11, text="Power", font=font1, padx=270, pady=5, fg="#3A98B9", bd=1, borderwidth=2,
                      relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Work and Time.
    work_label = tk.Label(popup_window11, text="Work (J): ", font=("Terakatal", 14), bg="#444654")
    work_label.grid(row=1, column=0)
    work_entry = tk.Entry(popup_window11, width=15, font="sans-serif")
    work_entry.grid(row=1, column=1, padx=5, pady=5)

    time_label = tk.Label(popup_window11, text="Time (s):", font=("Terakatal", 14), bg="#444654")
    time_label.grid(row=2, column=0)
    time_entry = tk.Entry(popup_window11, width=15, font="sans-serif")
    time_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window11, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_power(work_entry, time_entry,
                                                                 power_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window11, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear11(work_entry, time_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Power.
    power_label = tk.Label(popup_window11, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    power_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window11, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window11, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window11, height=4, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    Def = """POWER:
        Power is the rate at which work is done or energy is transferred, per unit 
time. It is the amount of energy per unit time that is consumed or produced by 
a system or device."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window11, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window11, height=7, width=68, font=("Terakatal", 12), bg="grey", borderwidth=1)
    For1 = """The formula for Power is:
       P = W / t
       
    where:
       P = Power
       W = Work
       t = Time"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window11.mainloop()


# Create Popup window for Angular Velocity
def popup12():
    popup_window12 = tk.Toplevel(root, bg="#444654")
    popup_window12.title("Calculator")
    popup_window12.geometry("620x640")
    popup_window12.resizable(height=False, width=False)
    # Create Angular velocity layout
    # Create a label for Angular Velocity.
    label1 = tk.Label(popup_window12, text="Angular Velocity", font=font1, padx=220, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Linear Velocity and Radius.
    linear_velocity_label = tk.Label(popup_window12, text="Linear Velocity (m/s): ", font=("Terakatal", 14),
                                     bg="#444654")
    linear_velocity_label.grid(row=1, column=0)
    linear_velocity_entry = tk.Entry(popup_window12, width=15, font="sans-serif")
    linear_velocity_entry.grid(row=1, column=1, padx=5, pady=5)

    radius_label = tk.Label(popup_window12, text="Radius (m):", font=("Terakatal", 14), bg="#444654")
    radius_label.grid(row=2, column=0)
    radius_entry = tk.Entry(popup_window12, width=15, font="sans-serif")
    radius_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window12, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_angular_velocity(linear_velocity_entry, radius_entry,
                                                                            angular_velocity_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window12, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear12(linear_velocity_entry, radius_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Angular Velocity.
    angular_velocity_label = tk.Label(popup_window12, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    angular_velocity_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window12, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window12, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window12, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """ANGULAR VELOCITY:
           Angular velocity is a measure of how fast an object rotates or 
moves in a circular or rotational motion. It is defined as the rate of 
change of angular displacement with respect to time. Angular velocity is 
a vector quantity, meaning it has both magnitude and direction. """
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window12, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window12, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Angular Velocity is:
       ω = v / r
       
    where:
       ω = Angular Velocity
       v = Linear Velocity
       r = Radius"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")
    # Insert the Formula

    T2.insert(tk.END, For1)
    popup_window12.mainloop()


# Create Popup window for Angular Acceleration
def popup13():
    popup_window13 = tk.Toplevel(root, bg="#444654")
    popup_window13.title("Calculator")
    popup_window13.geometry("635x650")
    popup_window13.resizable(height=False, width=False)
    # Create Angular Acceleration layout
    # Create a label for Angular Acceleration.
    label1 = tk.Label(popup_window13, text="Angular Acceleration", font=font1, padx=204, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Torque and Moment of inertia.
    torque_label = tk.Label(popup_window13, text="Angular Velocity (rad/s): ", font=("Terakatal", 14), bg="#444654")
    torque_label.grid(row=1, column=0)
    torque_entry = tk.Entry(popup_window13, width=15, font="sans-serif")
    torque_entry.grid(row=1, column=1, padx=5, pady=5)

    moment_of_inertia_label = tk.Label(popup_window13, text="Time (s):", font=("Terakatal", 14), bg="#444654")
    moment_of_inertia_label.grid(row=2, column=0)
    moment_of_inertia_entry = tk.Entry(popup_window13, width=15, font="sans-serif")
    moment_of_inertia_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window13, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_angular_acceleration(torque_entry, moment_of_inertia_entry,
                                                                                angular_acceleration_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window13, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear13(torque_entry, moment_of_inertia_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Angular Acceleration.
    angular_acceleration_label = tk.Label(popup_window13, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    angular_acceleration_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window13, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window13, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window13, height=5, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """ANGULAR ACCELERATION:
               Angular acceleration of an object undergoing circular motion is 
defined as the rate with which its angular velocity changes with time. 
Angular acceleration is a vector quantity, meaning it has both magnitude 
and direction."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window13, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window13, height=7, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Angular Acceleration is:
       α = θ / t
           
    Where:
       α = Angular Acceleration
       θ = Angular Velocity
       t = Time"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window13.mainloop()


# Create Popup window for Torque
def popup14():
    popup_window14 = tk.Toplevel(root, bg="#444654")
    popup_window14.title("Calculator")
    popup_window14.geometry("625x660")
    popup_window14.resizable(height=False, width=False)
    # Create a Torque layout
    # Create a label for Torque.
    label1 = tk.Label(popup_window14, text="Torque", font=font1, padx=270, pady=5, fg="#3A98B9", bd=1, borderwidth=2,
                      relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Force and Lever Arm Length.
    force_label = tk.Label(popup_window14, text="Force (N): ", font=("Terakatal", 14), bg="#444654")
    force_label.grid(row=1, column=0)
    force_entry = tk.Entry(popup_window14, width=15, font="sans-serif")
    force_entry.grid(row=1, column=1, padx=5, pady=5)

    lever_arm_length_label = tk.Label(popup_window14, text="Lever Arm Length (m):", font=("Terakatal", 14),
                                      bg="#444654")
    lever_arm_length_label.grid(row=2, column=0)
    lever_arm_length_entry = tk.Entry(popup_window14, width=15, font="sans-serif")
    lever_arm_length_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window14, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_torque(force_entry, lever_arm_length_entry,
                                                                  torque_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window14, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear14(force_entry, lever_arm_length_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Torque.
    torque_label = tk.Label(popup_window14, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    torque_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window14, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window14, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window14, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """TORQUE:
              Torque, also known as moment or moment of force, is a measure 
of the rotational force applied to an object around a specific point or 
axis. It is a vector quantity, meaning it has both magnitude and direction
Torque is responsible for causing objects to rotate or change their 
rotational motion."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window14, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window14, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Torque is:
       τ = F.r
       
    where:
       τ = Torque
       F = Force
       r = Lever Arm Length"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window14.mainloop()


# Create Popup window for Moment of Inertia
def popup15():
    popup_window15 = tk.Toplevel(root, bg="#444654")
    popup_window15.title("Calculator")
    popup_window15.geometry("625x690")
    popup_window15.resizable(height=False, width=False)
    # Create a Moment of Inertia layout
    # Create a label for Moment of Inertia.
    label1 = tk.Label(popup_window15, text="Moment of Inertia", font=font1, padx=215, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Mass and Distance.
    mass_label = tk.Label(popup_window15, text="Mass (kg): ", font=("Terakatal", 14), bg="#444654")
    mass_label.grid(row=1, column=0)
    mass_entry = tk.Entry(popup_window15, width=15, font="sans-serif")
    mass_entry.grid(row=1, column=1, padx=5, pady=5)

    distance_label = tk.Label(popup_window15, text="Distance (m): ", font=("Terakatal", 14), bg="#444654")
    distance_label.grid(row=2, column=0, padx=5, pady=5)
    distance_entry = tk.Entry(popup_window15, width=15, font="sans-serif")
    distance_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window15, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_moment_of_inertia(mass_entry, distance_entry,
                                                                             moment_of_inertia_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window15, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear15(mass_entry, distance_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Moment of Inertia.
    moment_of_inertia_label = tk.Label(popup_window15, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    moment_of_inertia_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window15, width=620, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window15, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window15, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """MOMENT OF INERTIA:
               The moment of inertia is defined as the quantity expressed by 
the body resisting angular acceleration, which is the sum of the product 
of the mass of every particle with its square of the distance from the axis of rotation. Moment of inertia is a scalar quantity, and it depends on the 
shape of the object and the location of its mass with respect to the axis 
of rotation."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window15, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window15, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Moment of inertia is:
       I = m.r²
       
    where:
       I = Moment of inertia
       m = Mass
       r = Distance"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window15.mainloop()


# Create Popup window for Angular Momentum
def popup16():
    popup_window16 = tk.Toplevel(root, bg="#444654")
    popup_window16.title("Calculator")
    popup_window16.geometry("655x690")
    popup_window16.resizable(height=False, width=False)
    # Create Angular Momentum layout
    # Create a label for Angular Momentum.
    label1 = tk.Label(popup_window16, text="Angular Momentum", font=font1, padx=220, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Moment of Inertia and Distance.
    moment_of_inertia_label = tk.Label(popup_window16, text="Moment of Inertia (kgm²): ", font=("Terakatal", 14),
                                       bg="#444654")
    moment_of_inertia_label.grid(row=1, column=0)
    moment_of_inertia_entry = tk.Entry(popup_window16, width=15, font="sans-serif")
    moment_of_inertia_entry.grid(row=1, column=1, padx=5, pady=5)

    distance_label = tk.Label(popup_window16, text="Angular Velocity (rad/s): ", font=("Terakatal", 14), bg="#444654")
    distance_label.grid(row=2, column=0)
    distance_entry = tk.Entry(popup_window16, width=15, font="sans-serif")
    distance_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window16, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_angular_momentum(moment_of_inertia_entry, distance_entry,
                                                                            angular_momentum_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window16, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear16(moment_of_inertia_entry, distance_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Angular Momentum.
    angular_momentum_label = tk.Label(popup_window16, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    angular_momentum_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window16, width=655, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window16, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window16, height=7, width=65, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """ANGULAR MOMENTUM:
            Angular momentum is a measure of an object's rotational motion 
around a specific axis. It is a vector quantity, meaning it has both magnitude and direction. Angular momentum depends on both the moment of inertia 
and the angular velocity of the object.Mathematically, angular momentum 
(L) is defined as the cross product of the moment of inertia (I) and the 
angular velocity (ω) of the object.
"""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window16, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window16, height=7, width=65, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Angular Momentum is:
       L = I.ω
       
    Where:
       L = Angular momentum
       I = Moment of inertia
       ω = Angular velocity"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window16.mainloop()


# Create Popup window for Universal Gravitation
def popup17():
    popup_window17 = tk.Toplevel(root, bg="#444654")
    popup_window17.title("Calculator")
    popup_window17.geometry("655x690")
    popup_window17.resizable(height=False, width=False)
    # Create Universal Gravitation layout
    # Create label for Universal Gravitation
    label1 = tk.Label(popup_window17, text="Universal Gravitation", font=font1, padx=210, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    # Create labels and entries for First mass, Second mass and Distance.
    first_mass_label = tk.Label(popup_window17, text="First mass (kg): ", font=("Terakatal", 14), bg="#444654")
    first_mass_label.grid(row=1, column=0)
    first_mass_entry = tk.Entry(popup_window17, width=15, font="sans-serif")
    first_mass_entry.grid(row=1, column=1, padx=5, pady=5)

    second_mass1_label = tk.Label(popup_window17, text="Second mass (kg): ", font=("Terakatal", 14), bg="#444654")
    second_mass1_label.grid(row=2, column=0)
    second_mass1_entry = tk.Entry(popup_window17, width=15, font="sans-serif")
    second_mass1_entry.grid(row=2, column=1, padx=5, pady=5)

    distance_label = tk.Label(popup_window17, text="Distance (m): ", font=("Terakatal", 14), bg="#444654")
    distance_label.grid(row=3, column=0)
    distance_entry = tk.Entry(popup_window17, width=15, font="sans-serif")
    distance_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window17, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_universal_gravitation(first_mass_entry, second_mass1_entry,
                                                                                 distance_entry,
                                                                                 universal_gravitation_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    # Create a label to display the Universal Gravitation result.
    universal_gravitation_label = tk.Label(popup_window17, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    universal_gravitation_label.grid(row=5, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window17, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear17(first_mass_entry, second_mass1_entry, distance_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window17, width=655, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window17, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window17, height=6, width=65, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """UNIVERSAL GRAVITATION:
                  Newton's Law of Universal Gravitation states that every particle in the universe attracts every other particle with a force directly proportional 
to the product of their masses and inversely proportional to the square of 
their distance.."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window17, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window17, height=7, width=65, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Moment of inertia is:
       F = G.(m1.m2) / r²
    Where:
       F = Force
      m1 = First mass
      m2 = Second mass
       r = Distance"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window17.mainloop()


# Create Popup window for Simple Pendulum
def popup18():
    popup_window18 = tk.Toplevel(root, bg="#444654")
    popup_window18.title("Calculator")
    popup_window18.geometry("625x550")
    popup_window18.resizable(height=False, width=False)
    # Create Simple Pendulum layout
    # Create a label for Simple Pendulum.
    label1 = tk.Label(popup_window18, text="Simple Pendulum", font=font1, padx=215, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Length of string.
    length_of_string_label = tk.Label(popup_window18, text="Length of string (m): ", font=("Terakatal", 14),
                                      bg="#444654")
    length_of_string_label.grid(row=1, column=0)
    length_of_string_entry = tk.Entry(popup_window18, width=15, font="sans-serif")
    length_of_string_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window18, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_period(length_of_string_entry, period_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window18, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear18(length_of_string_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Period.
    period_label = tk.Label(popup_window18, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    period_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window18, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window18, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window18, height=4, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """SIMPLE PENDULUM:
                     A simple pendulum consists of a small metal ball (called bob) or a mass suspended from a fixed point by a long thread such that the 
bob is free to swing back and forth under the influence of gravity."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window18, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window18, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Simple Pendulum is:
       T = 2π.√(L / g)
    Where:
       T = Period
       L = Length of string"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window18.mainloop()


# Create Popup window for Frequency
def popup19():
    popup_window19 = tk.Toplevel(root, bg="#444654")
    popup_window19.title("Calculator")
    popup_window19.geometry("625x550")
    popup_window19.resizable(height=False, width=False)
    # Create Frequency layout
    # Create a label for Frequency.
    label1 = tk.Label(popup_window19, text="Frequency", font=font1, padx=250, pady=5, fg="#3A98B9", bd=1, borderwidth=2,
                      relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Period.
    period_label = tk.Label(popup_window19, text="Period (s): ", font=("Terakatal", 14), bg="#444654")
    period_label.grid(row=1, column=0)
    period_entry = tk.Entry(popup_window19, width=15, font="sans-serif")
    period_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window19, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_frequency(period_entry, frequency_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window19, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear19(period_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Frequency.
    frequency_label = tk.Label(popup_window19, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    frequency_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window19, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window19, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window19, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """FREQUENCY:
            In physics, the term frequency refers to the number of waves that pass a fixed point in unit time. It also describes the number of cycles or 
vibrations undergone during one unit of time by a body in periodic 
motion."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window19, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window19, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Frequency is:
       f = 1 / T
    Where:
       f = Frequency
       T = Period"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window19.mainloop()


# Create Popup window for Density
def popup20():
    popup_window20 = tk.Toplevel(root, bg="#444654")
    popup_window20.title("Calculator")
    popup_window20.geometry("625x620")
    popup_window20.resizable(height=False, width=False)
    # Create Density layout
    # Create a label for Density.
    label1 = tk.Label(popup_window20, text="Density", font=font1, padx=260, pady=5, fg="#3A98B9", bd=1, borderwidth=2,
                      relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Mass and Volume.
    mass_label = tk.Label(popup_window20, text="Mass (kg): ", font=("Terakatal", 14), bg="#444654")
    mass_label.grid(row=1, column=0)
    mass_entry = tk.Entry(popup_window20, width=15, font="sans-serif")
    mass_entry.grid(row=1, column=1, padx=5, pady=5)

    volume_label = tk.Label(popup_window20, text="Volume (m³): ", font=("Terakatal", 14), bg="#444654")
    volume_label.grid(row=2, column=0)
    volume_entry = tk.Entry(popup_window20, width=15, font="sans-serif")
    volume_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window20, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_density(mass_entry, volume_entry, density_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window20, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear20(mass_entry, volume_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Density.
    density_label = tk.Label(popup_window20, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    density_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window20, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window20, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window20, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """DENSITY:
                Density refers to the measurement of the amount of mass of a 
substance per unit of volume. This measurement of a pure substance has the same value as its mass concentration. Densities vary with different 
materials or substances. Moreover, this particular measurement of a 
material can be relevant to purity, buoyancy, and packaging."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window20, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window20, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Density is:
       ρ = m / V
    Where:
       ρ = Density
       m = Mass
       V = Volume"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window20.mainloop()


# Create Popup window for Pressure
def popup21():
    popup_window21 = tk.Toplevel(root, bg="#444654")
    popup_window21.title("Calculator")
    popup_window21.geometry("595x580")
    popup_window21.resizable(height=False, width=False)
    # Create Pressure layout
    # Create a label for Pressure.
    label1 = tk.Label(popup_window21, text="Pressure", font=font1, padx=220, pady=5, fg="#3A98B9", bd=1, borderwidth=2,
                      relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Force and Area.
    force_label = tk.Label(popup_window21, text="Force (N): ", font=("Terakatal", 14), bg="#444654")
    force_label.grid(row=1, column=0)
    force_entry = tk.Entry(popup_window21, width=15, font="sans-serif")
    force_entry.grid(row=1, column=1, padx=5, pady=5)

    area_label = tk.Label(popup_window21, text="Area (m²): ", font=("Terakatal", 14), bg="#444654")
    area_label.grid(row=2, column=0)
    area_entry = tk.Entry(popup_window21, width=15, font="sans-serif")
    area_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window21, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_pressure(force_entry, area_entry, pressure_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window21, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear21(force_entry, area_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Pressure.
    pressure_label = tk.Label(popup_window21, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    pressure_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window21, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window21, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window21, height=4, width=59, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """PRESSURE:
             Pressure is defined as the force per unit area applied on a 
surface. It is a measure of how much force is distributed over a given 
area."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window21, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window21, height=5, width=59, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Pressure is:
       P = F / A
    Where:
       P = Pressure
       F = Force
       A = Area"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window21.mainloop()


# Create Popup window for Kinematic Viscosity
def popup22():
    popup_window22 = tk.Toplevel(root, bg="#444654")
    popup_window22.title("Calculator")
    popup_window22.geometry("625x620")
    popup_window22.resizable(height=False, width=False)
    # Create Kinematic Viscosity layout
    # Create a label for Kinematic Viscosity.
    label1 = tk.Label(popup_window22, text="Kinematic Viscosity", font=font1, padx=205, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Viscosity and Density.
    viscosity_label = tk.Label(popup_window22, text="Viscosity (Ns/m²): ", font=("Terakatal", 14), bg="#444654")
    viscosity_label.grid(row=1, column=0)
    viscosity_entry = tk.Entry(popup_window22, width=15, font="sans-serif")
    viscosity_entry.grid(row=1, column=1, padx=5, pady=5)

    density_label = tk.Label(popup_window22, text="Density (kg/m³): ", font=("Terakatal", 14), bg="#444654")
    density_label.grid(row=2, column=0)
    density_entry = tk.Entry(popup_window22, width=15, font="sans-serif")
    density_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window22, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_kinematic_viscosity(viscosity_entry, density_entry,
                                                                               kinematic_viscosity_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window22, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear22(viscosity_entry, density_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Kinematic Viscosity.
    kinematic_viscosity_label = tk.Label(popup_window22, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    kinematic_viscosity_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window22, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window22, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window22, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """KINEMATIC VISCOSITY:
             Kinematic viscosity is a measure of a fluid's resistance to flow 
due to internal friction and is defined as the ratio of dynamic viscosity to density. In other words, kinematic viscosity is the measure of the fluid's 
resistance to flow under its own weight."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window22, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window22, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Kinematic Viscosity is:
       ν = μ / ρ
    Where:
       ν = Kinematic Viscosity
       μ = Viscosity
       ρ = Density"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window22.mainloop()


# Create Popup window for Surface Tension
def popup23():
    popup_window23 = tk.Toplevel(root, bg="#444654")
    popup_window23.title("Calculator")
    popup_window23.geometry("635x600")
    popup_window23.resizable(height=False, width=False)
    # Create Surface Tension layout
    # Create a label for Surface Tension.
    label1 = tk.Label(popup_window23, text="Surface Tension", font=font1, padx=230, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Force and Length.
    force_label = tk.Label(popup_window23, text="Force (N): ", font=("Terakatal", 14), bg="#444654")
    force_label.grid(row=1, column=0)
    force_entry = tk.Entry(popup_window23, width=15, font="sans-serif")
    force_entry.grid(row=1, column=1, padx=5, pady=5)

    length_label = tk.Label(popup_window23, text="Length (m): ", font=("Terakatal", 14), bg="#444654")
    length_label.grid(row=2, column=0)
    length_entry = tk.Entry(popup_window23, width=15, font="sans-serif")
    length_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window23, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_surface_tension(force_entry, length_entry,
                                                                           surface_tension_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window23, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear22(force_entry, length_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Surface Tension.
    surface_tension_label = tk.Label(popup_window23, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    surface_tension_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window23, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window23, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window23, height=4, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """SURFACE TENSION:
             Surface tension is the tension of the surface film of a liquid caused by the attraction of the particles in the surface layer by the bulk of the 
liquid, which tends to minimise surface area."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window23, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window23, height=6, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Surface Tension is:
       γ = F / 2L
    Where:
       γ = Surface Tension
       F = Force
       L = Length"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window23.mainloop()


# Popup window for Thermal Physics formula
# Create Popup window for Sensible Heat
def popup24():
    popup_window24 = tk.Toplevel(root, bg="#444654")
    popup_window24.title("Calculator")
    popup_window24.geometry("625x650")
    popup_window24.resizable(height=False, width=False)
    # Create Sensible Heat layout
    # Create label for Sensible Heat
    label1 = tk.Label(popup_window24, text="Sensible Heat", font=font1, padx=230, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    # Create labels and entries for Mass, Specific heat capacity and Change in temperature.
    mass_label = tk.Label(popup_window24, text="Mass (kg): ", font=("Terakatal", 14), bg="#444654")
    mass_label.grid(row=1, column=0)
    mass_entry = tk.Entry(popup_window24, width=15, font="sans-serif")
    mass_entry.grid(row=1, column=1, padx=5, pady=5)

    specific_heat_capacity_label = tk.Label(popup_window24, text="Specific heat capacity (J/kgK): ",
                                            font=("Terakatal", 14), bg="#444654")
    specific_heat_capacity_label.grid(row=2, column=0)
    specific_heat_capacity_entry = tk.Entry(popup_window24, width=15, font="sans-serif")
    specific_heat_capacity_entry.grid(row=2, column=1, padx=5, pady=5)

    change_in_temperature_label = tk.Label(popup_window24, text="Change in temperature (K): ", font=("Terakatal", 14),
                                           bg="#444654")
    change_in_temperature_label.grid(row=3, column=0)
    change_in_temperature_entry = tk.Entry(popup_window24, width=15, font="sans-serif")
    change_in_temperature_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window24, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_sensible_heat(mass_entry, specific_heat_capacity_entry,
                                                                         change_in_temperature_entry,
                                                                         sensible_heat_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    # Create a label to display the Sensible Heat result.
    sensible_heat_label = tk.Label(popup_window24, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    sensible_heat_label.grid(row=5, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window24, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear24(mass_entry, specific_heat_capacity_entry,
                                                     change_in_temperature_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window24, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window24, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window24, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """SENSIBLE HEAT:
             Sensible heat is the heat exchanged by the object that causes a 
change in temperature of the object without changing its phase."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window24, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window24, height=8, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Sensible Heat is:
       Q = m.c.ΔT
       
    Where:
       Q = Sensible Heat
       m = Mass
       c = Specific heat capacity
      ΔT = Change in temperature"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window24.mainloop()


# Create Popup window for Latent Heat
def popup25():
    popup_window25 = tk.Toplevel(root, bg="#444654")
    popup_window25.title("Calculator")
    popup_window25.geometry("625x600")
    popup_window25.resizable(height=False, width=False)
    # Create Latent Heat layout
    # Create a label for Latent Heat.
    label1 = tk.Label(popup_window25, text="Latent Heat", font=("Calbiri", 17, "bold"), padx=235, pady=5, fg="#3A98B9",
                      bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Mass and Specific latent heat.
    mass_label = tk.Label(popup_window25, text="Mass (kg): ", font=("Terakatal", 14), bg="#444654")
    mass_label.grid(row=1, column=0)
    mass_entry = tk.Entry(popup_window25, width=15, font="sans-serif")
    mass_entry.grid(row=1, column=1, padx=5, pady=5)

    specific_latent_heat_label = tk.Label(popup_window25, text="Specific latent heat (kJ/kg): ", font=("Terakatal", 14),
                                          bg="#444654")
    specific_latent_heat_label.grid(row=2, column=0)
    specific_latent_heat_entry = tk.Entry(popup_window25, width=15, font="sans-serif")
    specific_latent_heat_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window25, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_latent_heat(mass_entry, specific_latent_heat_entry,
                                                                       latent_heat_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window25, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear25(mass_entry, specific_latent_heat_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Latent Heat result.
    latent_heat_label = tk.Label(popup_window25, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    latent_heat_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window25, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window25, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window25, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """LATENT HEAT:
             Latent heat is the heat exchange by the material at a constant 
temperature while changing its phase."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window25, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window25, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Latent Heat is:
       Q = m.L

    Where:
       Q = Sensible Heat
       m = Mass
       L = Specific latent heat"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window25.mainloop()


# Create Popup window for Ideal Gas Law
def popup26():
    popup_window26 = tk.Toplevel(root, bg="#444654")
    popup_window26.title("Calculator")
    popup_window26.geometry("625x750")
    popup_window26.resizable(height=False, width=False)
    # Create Ideal Gas Law layout
    # Create label for Ideal Gas Law
    label1 = tk.Label(popup_window26, text="Ideal Gas Law ", font=("Calbiri", 17, "bold"), padx=220, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Volume, Amount of Substance and Temperature.
    volume_label = tk.Label(popup_window26, text="Volume (m³): ", font=("Terakatal", 14), bg="#444654")
    volume_label.grid(row=1, column=0)
    volume_entry = tk.Entry(popup_window26, width=15, font="sans-serif")
    volume_entry.grid(row=1, column=1, padx=5, pady=5)

    amount_of_substance_label = tk.Label(popup_window26, text="Amount of Substance (mol): ",
                                         font=("Terakatal", 14), bg="#444654")
    amount_of_substance_label.grid(row=2, column=0)
    amount_of_substance_entry = tk.Entry(popup_window26, width=15, font="sans-serif")
    amount_of_substance_entry.grid(row=2, column=1, padx=5, pady=5)

    temperature_label = tk.Label(popup_window26, text="Temperature (K): ", font=("Terakatal", 14), bg="#444654")
    temperature_label.grid(row=3, column=0)
    temperature_entry = tk.Entry(popup_window26, width=15, font="sans-serif")
    temperature_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window26, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_ideal_gas_law(volume_entry, amount_of_substance_entry,
                                                                         temperature_entry,
                                                                         pressure_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    # Create a label to display the Ideal Gas Law result.
    pressure_label = tk.Label(popup_window26, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    pressure_label.grid(row=5, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window26, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear26(volume_entry, amount_of_substance_entry,
                                                     temperature_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window26, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window26, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window26, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """IDEAL GAS LAW:
             The ideal gas law is the equation of state of a hypothetical ideal gas. It is a good approximation of the behaviour of many gases under 
many conditions, although it has several limitations. The state of an ideal gas is determined by the macroscopic and microscopic parameters like 
pressure, volume, temperature."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window26, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window26, height=9, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Ideal Gas Law is:
       P . V = n . R. T

    Where:
       P = Pressure
       V = Volume
       n = Amount of substance
       R = Gas Constant(8.3145 J / mol·K)
       T = Temperature"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window26.mainloop()


# Create Popup window for Stefan Boltzmann Law
def popup27():
    popup_window27 = tk.Toplevel(root, bg="#444654")
    popup_window27.title("Calculator")
    popup_window27.geometry("625x760")
    popup_window27.resizable(height=False, width=False)
    # Create Stefan_Boltzmann Law layout
    # Create label for Stefan_Boltzmann Law
    label1 = tk.Label(popup_window27, text="Stefan-Boltzmann Law", font=("Calbiri", 17, "bold"), padx=170, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Area, Emissivity and Temperature.
    area_label = tk.Label(popup_window27, text="Area (m²): ", font=("Terakatal", 14), bg="#444654")
    area_label.grid(row=1, column=0)
    area_entry = tk.Entry(popup_window27, width=15, font="sans-serif")
    area_entry.grid(row=1, column=1, padx=5, pady=5)

    emissivity_label = tk.Label(popup_window27, text="Emissivity : ",
                                font=("Terakatal", 14), bg="#444654")
    emissivity_label.grid(row=2, column=0)
    emissivity_entry = tk.Entry(popup_window27, width=15, font="sans-serif")
    emissivity_entry.grid(row=2, column=1, padx=5, pady=5)

    temperature_label = tk.Label(popup_window27, text="Temperature (K): ", font=("Terakatal", 14), bg="#444654")
    temperature_label.grid(row=3, column=0)
    temperature_entry = tk.Entry(popup_window27, width=15, font="sans-serif")
    temperature_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window27, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_power1(area_entry, emissivity_entry,
                                                                  temperature_entry,
                                                                  power_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    # Create a label to display the Stefan-Boltzmann Law(Power) result.
    power_label = tk.Label(popup_window27, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    power_label.grid(row=5, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window27, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear27(area_entry, emissivity_entry,
                                                     temperature_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window27, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window27, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window27, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """STEFAN BOLTZMANN LAW:
                    The Stefan-Boltzmann law, also known as Stefan's law, is a 
fundamental law of thermodynamics that relates the total amount of 
energy radiated by a black body to its temperature. It states that the 
total radiant energy (E) emitted by a black body per unit surface area (A) 
is proportional to the fourth power of its absolute temperature (T)."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window27, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window27, height=9, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Stefan Boltzmann Law is:
       P = A.ε.σ.T^4

    Where:
       P = Power
       A = Area
       ε = Emissivity
       σ = Stefan Boltzmann constant
       T = Temperature"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window27.mainloop()


# Create Popup window for Thermal Energy
def popup28():
    popup_window28 = tk.Toplevel(root, bg="#444654")
    popup_window28.title("Calculator")
    popup_window28.geometry("625x720")
    popup_window28.resizable(height=False, width=False)
    # Create Thermal Energy layout
    # Create a label for Thermal Energy.
    label1 = tk.Label(popup_window28, text="Thermal Energy", font=("Calbiri", 17, "bold"), padx=210, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Number of particles and temperature.
    number_of_particles_label = tk.Label(popup_window28, text="Number of Particles : ", font=("Terakatal", 14),
                                         bg="#444654")
    number_of_particles_label.grid(row=1, column=0)
    number_of_particles_entry = tk.Entry(popup_window28, width=15, font="sans-serif")
    number_of_particles_entry.grid(row=1, column=1, padx=5, pady=5)

    temperature_label = tk.Label(popup_window28, text="Temperature (K): ", font=("Terakatal", 14), bg="#444654")
    temperature_label.grid(row=2, column=0)
    temperature_entry = tk.Entry(popup_window28, width=15, font="sans-serif")
    temperature_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window28, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_thermal_energy(number_of_particles_entry, temperature_entry,
                                                                          thermal_energy_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window28, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear28(number_of_particles_entry, temperature_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Thermal Energy result.
    thermal_energy_label = tk.Label(popup_window28, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    thermal_energy_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window28, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window28, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window28, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """THERMAL ENERGY:
                Thermal energy refers to the form of energy that is associated 
with the temperature of a substance or a system. It is the energy that 
arises from the motion and interaction of particles at the atomic or 
molecular level within a substance, which determines its temperature. 
The higher the temperature of a substance, the greater the thermal 
energy it possesses."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window28, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window28, height=8, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Thermal Energy is:
       U = 3/2.N.k.T

    where:
       U = Thermal energy of the ideal gas
       N = Number of particles
       k = Boltzmann Constant(1.380649 × 10^-23  JK)
       T = Temperature"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window28.mainloop()


# Create Popup window for Gibbs free energy
def popup29():
    popup_window29 = tk.Toplevel(root, bg="#444654")
    popup_window29.title("Calculator")
    popup_window29.geometry("635x710")
    popup_window29.resizable(height=False, width=False)
    # Create Gibbs free energy layout
    # Create label for Gibbs free energy
    label1 = tk.Label(popup_window29, text="Gibbs free energy", font=("Calbiri", 17, "bold"), padx=200, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    # Create labels and entries for Enthalpy, Entropy and Temperature.
    enthalpy_label = tk.Label(popup_window29, text="Enthalpy (J): ", font=("Terakatal", 14), bg="#444654")
    enthalpy_label.grid(row=1, column=0)
    enthalpy_entry = tk.Entry(popup_window29, width=15, font="sans-serif")
    enthalpy_entry.grid(row=1, column=1, padx=5, pady=5)

    temperature_label = tk.Label(popup_window29, text="Temperature (K): ",
                                 font=("Terakatal", 14), bg="#444654")
    temperature_label.grid(row=2, column=0, padx=5, pady=5)
    temperature_entry = tk.Entry(popup_window29, width=15, font="sans-serif")
    temperature_entry.grid(row=2, column=1, padx=5, pady=5)

    entropy_label = tk.Label(popup_window29, text="Entropy (J/K): ", font=("Terakatal", 14), bg="#444654")
    entropy_label.grid(row=3, column=0)
    entropy_entry = tk.Entry(popup_window29, width=15, font="sans-serif")
    entropy_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window29, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_gibbs_free_energy(enthalpy_entry, temperature_entry,
                                                                             entropy_entry,
                                                                             gibbs_free_energy_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    # Create a label to display the Gibbs free energy result.
    gibbs_free_energy_label = tk.Label(popup_window29, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    gibbs_free_energy_label.grid(row=5, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window29, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear29(enthalpy_entry, temperature_entry,
                                                     entropy_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window29, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window29, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window29, height=5, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """GIBBS FREE ENERGY:
             Gibbs free energy, also known as the Gibbs function, Gibbs energy or free enthalpy, is a quantity that is used to measure the maximum 
amount of work done in a thermodynamic system when the temperature 
and pressure are kept constant."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window29, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window29, height=8, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Gibbs free Energy is:
       G = H - TS

    where:
       G = Gibbs free energy 
       H = Enthalpy
       T = Temperature
       S = Entropy"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window29.mainloop()


# Create Popup window for Thermodynamic Work
def popup30():
    popup_window30 = tk.Toplevel(root, bg="#444654")
    popup_window30.title("Calculator")
    popup_window30.geometry("635x700")
    popup_window30.resizable(height=False, width=False)
    # Create Thermodynamic Work layout
    # Create a label for Thermodynamic Work.
    label1 = tk.Label(popup_window30, text="Thermodynamic Work", font=("Calbiri", 17, "bold"), padx=180, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Pressure and Volume.
    pressure_label = tk.Label(popup_window30, text="Pressure (pascal) : ", font=("Terakatal", 14), bg="#444654")
    pressure_label.grid(row=1, column=0)
    pressure_entry = tk.Entry(popup_window30, width=15, font="sans-serif")
    pressure_entry.grid(row=1, column=1, padx=5, pady=5)

    volume_label = tk.Label(popup_window30, text="volume (m³): ", font=("Terakatal", 14), bg="#444654")
    volume_label.grid(row=2, column=0)
    volume_entry = tk.Entry(popup_window30, width=15, font="sans-serif")
    volume_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window30, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_thermodynamic_work(pressure_entry, volume_entry,
                                                                              work_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window30, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear30(pressure_entry, volume_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Thermodynamic Work result.
    work_label = tk.Label(popup_window30, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    work_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window30, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window30, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window30, height=6, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """THERMODYNAMIC WORK:
             In thermodynamics, work is defined as a form of energy transfer 
that occurs when a force is applied to a system and the system undergoes a displacement in the direction of the applied force. Work is a scalar 
quantity that can be positive or negative, depending on the direction of 
the force and the displacement."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window30, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window30, height=8, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Thermodynamic work is:
       W = -P.dv

    where:
       W = Work
       P = Pressure
      dv = Volume"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window30.mainloop()


# Create Popup window for 1st Law of Thermodynamic
def popup31():
    popup_window31 = tk.Toplevel(root, bg="#444654")
    popup_window31.title("Calculator")
    popup_window31.geometry("605x640")
    popup_window31.resizable(height=False, width=False)
    # Create Law of Thermodynamic layout
    # Create a label for 1st Law of Thermodynamic.
    label1 = tk.Label(popup_window31, text="1st Law of Thermodynamic", font=("Calbiri", 17, "bold"), padx=130, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Quantity of heat and Work.
    quantity_of_heat_label = tk.Label(popup_window31, text="Quantity of heat (J) : ", font=("Terakatal", 14),
                                      bg="#444654")
    quantity_of_heat_label.grid(row=1, column=0)
    quantity_of_heat_entry = tk.Entry(popup_window31, width=15, font="sans-serif")
    quantity_of_heat_entry.grid(row=1, column=1, padx=5, pady=5)

    work_label = tk.Label(popup_window31, text="Work (J): ", font=("Terakatal", 14), bg="#444654")
    work_label.grid(row=2, column=0)
    work_entry = tk.Entry(popup_window31, width=15, font="sans-serif")
    work_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window31, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_internal_energy(quantity_of_heat_entry, work_entry,
                                                                           internal_energy_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window31, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear31(quantity_of_heat_entry, work_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Internal energy result.
    internal_energy_label = tk.Label(popup_window31, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    internal_energy_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window31, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window31, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window31, height=4, width=60, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """1st LAW OF THERMODYNAMIC:
                  The first law of thermodynamics, also known as the law of 
conservation of energy, states that energy can neither be created nor 
destroyed, but it can be changed from one form to another."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window31, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window31, height=7, width=60, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for 1st Law of Thermodynamic is:
       ΔU = Q - W

    where:
      ΔU = Internal energy
       Q = Quantity of heat
       W = Work"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window31.mainloop()


# Create Popup window for Entropy
def popup32():
    popup_window32 = tk.Toplevel(root, bg="#444654")
    popup_window32.title("Calculator")
    popup_window32.geometry("645x650")
    popup_window32.resizable(height=False, width=False)
    # Create Entropy layout
    # Create a label for Entropy.
    label1 = tk.Label(popup_window32, text="Entropy", font=("Calbiri", 17, "bold"), padx=265, pady=5, fg="#3A98B9",
                      bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Quantity of heat and Temperature.
    quantity_of_heat_label = tk.Label(popup_window32, text="Quantity of heat (J) : ", font=("Terakatal", 14),
                                      bg="#444654")
    quantity_of_heat_label.grid(row=1, column=0)
    quantity_of_heat_entry = tk.Entry(popup_window32, width=15, font="sans-serif")
    quantity_of_heat_entry.grid(row=1, column=1, padx=5, pady=5)

    temperature_label = tk.Label(popup_window32, text="Temperature (K): ", font=("Terakatal", 14), bg="#444654")
    temperature_label.grid(row=2, column=0)
    temperature_entry = tk.Entry(popup_window32, width=15, font="sans-serif")
    temperature_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window32, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_entropy(quantity_of_heat_entry, temperature_entry,
                                                                   entropy_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window32, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear32(quantity_of_heat_entry, temperature_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Internal energy result.
    entropy_label = tk.Label(popup_window32, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    entropy_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window32, width=645, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window32, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window32, height=5, width=64, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """ENTROPY:
             Entropy is a thermodynamic property that quantifies the degree of 
randomness, disorder, or chaos in a system. It is a measure of the 
distribution of energy or matter within a system, and how that distribution changes as a system undergoes a process or transformation."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window32, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window32, height=7, width=64, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Entropy is:
           ΔU = Q - W

        where:
          ΔU = Internal energy
           Q = Quantity of heat
           W = Work"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window32.mainloop()


# Create Popup window for Efficiency
def popup33():
    popup_window33 = tk.Toplevel(root, bg="#444654")
    popup_window33.title("Calculator")
    popup_window33.geometry("625x610")
    popup_window33.resizable(height=False, width=False)
    # Create Efficiency layout
    # Create a label for Efficiency.
    label1 = tk.Label(popup_window33, text="Efficiency", font=("Calbiri", 17, "bold"), padx=245, pady=5, fg="#3A98B9",
                      bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Thermal energy and Waste heat.
    thermal_energy_label = tk.Label(popup_window33, text="Thermal energy (J) : ", font=("Terakatal", 14), bg="#444654")
    thermal_energy_label.grid(row=1, column=0)
    thermal_energy_entry = tk.Entry(popup_window33, width=15, font="sans-serif")
    thermal_energy_entry.grid(row=1, column=1, padx=5, pady=5)

    waste_heat_label = tk.Label(popup_window33, text="Waste heat (J): ", font=("Terakatal", 14), bg="#444654")
    waste_heat_label.grid(row=2, column=0)
    waste_heat_entry = tk.Entry(popup_window33, width=15, font="sans-serif")
    waste_heat_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window33, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_thermal_efficiency(thermal_energy_entry, waste_heat_entry,
                                                                              thermal_efficiency_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window33, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear33(thermal_energy_entry, waste_heat_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Thermal efficiency result.
    thermal_efficiency_label = tk.Label(popup_window33, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    thermal_efficiency_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window33, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window33, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window33, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """EFFICIENCY:
             Efficiency is the ratio of the work performed by a machine or in a process to the total energy expended or heat consumed."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window33, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window33, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Efficiency is:
       η = 1 - Qo / Qi 

    where:
       η = Thermal efficiency 
      Q0 = Thermal energy
      Qi = Waste heat"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window33.mainloop()


# Create Popup window for C.O.P
def popup34():
    popup_window34 = tk.Toplevel(root, bg="#444654")
    popup_window34.title("Calculator")
    popup_window34.geometry("645x630")
    popup_window34.resizable(height=False, width=False)
    # Create C.O.P layout
    # Create a label for C.O.P.
    label1 = tk.Label(popup_window34, text="C.O.P", font=("Calbiri", 17, "bold"), padx=270, pady=5, fg="#3A98B9", bd=1,
                      borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Heat removed and Heat supplied.
    heat_removed_label = tk.Label(popup_window34, text="Heat removed (J) : ", font=("Terakatal", 14), bg="#444654")
    heat_removed_label.grid(row=1, column=0)
    heat_removed_entry = tk.Entry(popup_window34, width=15, font="sans-serif")
    heat_removed_entry.grid(row=1, column=1, padx=5, pady=5)

    heat_supplied_label = tk.Label(popup_window34, text="Heat supplied(J): ", font=("Terakatal", 14), bg="#444654")
    heat_supplied_label.grid(row=2, column=0)
    heat_supplied_entry = tk.Entry(popup_window34, width=15, font="sans-serif")
    heat_supplied_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window34, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_c_o_p(heat_removed_entry, heat_supplied_entry,
                                                                 c_o_p_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window34, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear35(heat_removed_entry, heat_supplied_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Coefficient of Performance result.
    c_o_p_label = tk.Label(popup_window34, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    c_o_p_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window34, width=645, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window34, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window34, height=4, width=64, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """COEFFICIENT OF PERFORMANCE:
             The coefficient of performance or COP of a heat pump, refrigerator or air conditioning system is a ratio of useful heating or cooling provided 
to work required. Higher COPs equate to lower operating costs."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window34, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window34, height=7, width=64, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Coefficient of Performance is:
    Kcop = Qc / Qh - Qc 

    where:
    Kcop = Coefficient of Performance 
      Qc = Heat removed
      Qh = Heat supplied"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window34.mainloop()


# Create Popup window for Periodic Waves
def popup35():
    popup_window35 = tk.Toplevel(root, bg="#444654")
    popup_window35.title("Calculator")
    popup_window35.geometry("605x610")
    popup_window35.resizable(height=False, width=False)
    # Create Periodic Waves layout
    # Create a label for Periodic Waves
    label1 = tk.Label(popup_window35, text="Periodic Waves", font=("Calbiri", 17, "bold"), padx=210, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Wavelength and Wave's frequency.
    wavelength_label = tk.Label(popup_window35, text="Wavelength (m) : ", font=("Terakatal", 14), bg="#444654")
    wavelength_label.grid(row=1, column=0)
    wavelength_entry = tk.Entry(popup_window35, width=15, font="sans-serif")
    wavelength_entry.grid(row=1, column=1, padx=5, pady=5)

    wave_frequency_label = tk.Label(popup_window35, text="Wave's frequency (1/s): ", font=("Terakatal", 14),
                                    bg="#444654")
    wave_frequency_label.grid(row=2, column=0)
    wave_frequency_entry = tk.Entry(popup_window35, width=15, font="sans-serif")
    wave_frequency_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window35, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_phase_speed(wavelength_entry, wave_frequency_entry,
                                                                       phase_speed_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window35, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear35(wavelength_entry, wave_frequency_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Phase speed result.
    phase_speed_label = tk.Label(popup_window35, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    phase_speed_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window35, width=605, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window35, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window35, height=3, width=60, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """PERIODIC WAVES:
             A periodic wave is a wave with a repeating continuous pattern 
which determines its wavelength and frequency."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window35, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window35, height=7, width=60, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Periodic Waves is:
       v = f λ 
       
    where:
       v = Phase speed
       f = Wave's frequency
       λ = Wavelength"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window35.mainloop()


# Create Popup window for Beat frequency
def popup36():
    popup_window36 = tk.Toplevel(root, bg="#444654")
    popup_window36.title("Calculator")
    popup_window36.geometry("635x650")
    popup_window36.resizable(height=False, width=False)
    # Create Beat frequency layout
    # Create a label for Beat frequency
    label1 = tk.Label(popup_window36, text="Beat frequency", font=("Calbiri", 17, "bold"), padx=220, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for High frequency and Low frequency.
    high_frequency_label = tk.Label(popup_window36, text="High frequency (Hz) : ", font=("Terakatal", 14), bg="#444654")
    high_frequency_label.grid(row=1, column=0)
    high_frequency_entry = tk.Entry(popup_window36, width=15, font="sans-serif")
    high_frequency_entry.grid(row=1, column=1, padx=5, pady=5)

    low_frequency_label = tk.Label(popup_window36, text="Low frequency (Hz): ", font=("Terakatal", 14), bg="#444654")
    low_frequency_label.grid(row=2, column=0, padx=5, pady=5)
    low_frequency_entry = tk.Entry(popup_window36, width=15, font="sans-serif")
    low_frequency_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window36, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_beat_frequency(high_frequency_entry, low_frequency_entry,
                                                                          beat_frequency_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window36, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear36(high_frequency_entry, low_frequency_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Beat frequency result.
    beat_frequency_label = tk.Label(popup_window36, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    beat_frequency_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window36, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window36, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window36, height=5, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """BEAT FREQUENCY:
            The beat frequency is equal to the complete value of the alteration in the frequency of the two waves. The count of beats per second is 
equivalent to the difference in frequencies of two waves is called beat 
frequency."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window36, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window36, height=7, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Beat Frequency is:
      fb = fh - fl  

    where:
      fb = Beat frequency
      fh = High frequency
      fl = Low frequency"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window36.mainloop()


# Create Popup window for Intensity
def popup37():
    popup_window37 = tk.Toplevel(root, bg="#444654")
    popup_window37.title("Calculator")
    popup_window37.geometry("605x600")
    popup_window37.resizable(height=False, width=False)
    # Create Intensity layout
    # Create a label for Intensity
    label1 = tk.Label(popup_window37, text="Intensity", font=("Calbiri", 17, "bold"), padx=240, pady=5, fg="#3A98B9",
                      bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Power radiated and Area.
    power_radiated_label = tk.Label(popup_window37, text="Power radiated (watt) : ", font=("Terakatal", 14),
                                    bg="#444654")
    power_radiated_label.grid(row=1, column=0)
    power_radiated_entry = tk.Entry(popup_window37, width=15, font="sans-serif")
    power_radiated_entry.grid(row=1, column=1, padx=5, pady=5)

    area_label = tk.Label(popup_window37, text="Area (m²): ", font=("Terakatal", 14), bg="#444654")
    area_label.grid(row=2, column=0)
    area_entry = tk.Entry(popup_window37, width=15, font="sans-serif")
    area_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window37, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_intensity(power_radiated_entry, area_entry,
                                                                     intensity_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window37, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear37(power_radiated_entry, area_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Intensity result.
    intensity_label = tk.Label(popup_window37, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    intensity_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window37, width=605, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window37, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window37, height=3, width=60, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """INTENSITY:
                The Intensity of waves is defined as the power delivered per unit area."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window37, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window37, height=7, width=60, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Intensity is:
       I = P / A
    
    where:
       I = Intensity
       P = Power radiated
       A = Area"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window37.mainloop()


# Create Popup window for Intensity Level
def popup38():
    popup_window38 = tk.Toplevel(root, bg="#444654")
    popup_window38.title("Calculator")
    popup_window38.geometry("635x650")
    popup_window38.resizable(height=False, width=False)
    # Create Intensity Level layout
    # Create a label for Intensity Level
    label1 = tk.Label(popup_window38, text="Intensity Level", font=("Calbiri", 17, "bold"), padx=220, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Sound intensity and Reference intensity.
    sound_intensity_label = tk.Label(popup_window38, text="Sound intensity (W/m²) : ", font=("Terakatal", 14),
                                     bg="#444654")
    sound_intensity_label.grid(row=1, column=0)
    sound_intensity_entry = tk.Entry(popup_window38, width=15, font="sans-serif")
    sound_intensity_entry.grid(row=1, column=1, padx=5, pady=5)

    reference_intensity_label = tk.Label(popup_window38, text="Reference intensity (W/m²): ", font=("Terakatal", 14),
                                         bg="#444654")
    reference_intensity_label.grid(row=2, column=0)
    reference_intensity_entry = tk.Entry(popup_window38, width=15, font="sans-serif")
    reference_intensity_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window38, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_sound_intensity_level(sound_intensity_entry,
                                                                                 reference_intensity_entry,
                                                                                 sound_intensity_level_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window38, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear38(sound_intensity_entry,
                                                     reference_intensity_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Sound intensity level result.
    sound_intensity_level_label = tk.Label(popup_window38, font=("Verdana", 14), fg="#0002a1", bg="#444654")
    sound_intensity_level_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window38, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window38, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window38, height=5, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """INTENSITY LEVEL:
             Intensity level refers to the measure of the loudness or brightness of a wave, such as sound or light. It is defined as the logarithm (base 10) 
of the ratio of the intensity of a wave to a reference intensity, typically the 
threshold of human perception. """
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window38, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window38, height=7, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Intensity level is:
      LI = 10.log10(I / Io)

    where:
       L = Sound Intensity Level
       I = Sound Intensity
      Io = Reference Intensity"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window38.mainloop()


# Create Popup window for Pressure Level
def popup39():
    popup_window39 = tk.Toplevel(root, bg="#444654")
    popup_window39.title("Calculator")
    popup_window39.geometry("625x640")
    popup_window39.resizable(height=False, width=False)
    # Create Pressure Level layout
    # Create a label for pressure Level
    label1 = tk.Label(popup_window39, text="Pressure Level", font=("Calbiri", 17, "bold"), padx=220, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Sound pressure and Reference pressure.
    sound_pressure_label = tk.Label(popup_window39, text="Sound pressure (Pa) : ", font=("Terakatal", 14), bg="#444654")
    sound_pressure_label.grid(row=1, column=0)
    sound_pressure_entry = tk.Entry(popup_window39, width=15, font="sans-serif")
    sound_pressure_entry.grid(row=1, column=1, padx=5, pady=5)

    reference_pressure_label = tk.Label(popup_window39, text="Reference pressure (Pa): ", font=("Terakatal", 14),
                                        bg="#444654")
    reference_pressure_label.grid(row=2, column=0)
    reference_pressure_entry = tk.Entry(popup_window39, width=15, font="sans-serif")
    reference_pressure_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window39, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_sound_pressure_level(sound_pressure_entry,
                                                                                reference_pressure_entry,
                                                                                sound_pressure_level_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window39, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear39(sound_pressure_entry,
                                                     reference_pressure_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Sound pressure level result.
    sound_pressure_level_label = tk.Label(popup_window39, font=("Verdana", 14), bg="#444654", fg="#0002a1")
    sound_pressure_level_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window39, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window39, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window39, height=4, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """PRESSURE LEVEL:
             Pressure level refers to the measure of the sound pressure of a 
wave relative to a reference sound pressure. It is a logarithmic scale used to quantify the loudness of a sound wave."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window39, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window39, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Pressure level is:
      LP = 20.log10(P / Po)

    where:
       L = Sound Pressure Level
       P = Sound Pressure
      Po = Reference Pressure"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window39.mainloop()


# Create Popup window for Index of Refraction
def popup40():
    popup_window40 = tk.Toplevel(root, bg="#444654")
    popup_window40.title("Calculator")
    popup_window40.geometry("625x620")
    popup_window40.resizable(height=False, width=False)
    # Create Index of Refraction layout
    # Create a label for Index of Refraction.
    label1 = tk.Label(popup_window40, text="Index of Refraction", font=("Calbiri", 17, "bold"), padx=190, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries Phase velocity of light.
    phase_velocity_of_light_label = tk.Label(popup_window40, text="Phase velocity of light (m/s): ",
                                             font=("Terakatal", 14), bg="#444654")
    phase_velocity_of_light_label.grid(row=1, column=0)
    phase_velocity_of_light_entry = tk.Entry(popup_window40, width=12, font="sans-serif")
    phase_velocity_of_light_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window40, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_refractive_index(phase_velocity_of_light_entry,
                                                                            refractive_index_label))
    calculate_button.grid(row=2, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window40, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear40(phase_velocity_of_light_entry))
    clear_button.grid(row=2, column=0, padx=5, pady=5)

    # Create a label to display the Refractive index.
    refractive_index_label = tk.Label(popup_window40, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    refractive_index_label.grid(row=3, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window40, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=4, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window40, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=5, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window40, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """INDEX OF REFRACTION:
             The index of refraction, or refractive index, is a measure of how 
fast light rays travel through a given medium. Alternatively, it could be 
said that the refractive index is the measure of the bending of a light ray when passing from one medium to another."""
    T.grid(row=6, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window40, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window40, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Index of Refraction is:
       n = c / v

    where:
       n = Refractive index
       v = Phase velocity of light
       c = Speed of Light"""
    T2.grid(row=8, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window40.mainloop()


# Create Popup window for Snell's Law
def popup41():
    popup_window41 = tk.Toplevel(root, bg="#444654")
    popup_window41.title("Calculator")
    popup_window41.geometry("685x730")
    popup_window41.resizable(height=False, width=False)
    # Create Snell's Law layout
    # Create label for Snell's Law
    label1 = tk.Label(popup_window41, text="Snell's Law", font=("Calbiri", 17, "bold"), padx=260, pady=5, fg="#3A98B9",
                      bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    # Create labels and entries for Angle of refraction, Refractive index of second medium and Refractive index of first medium.
    angle_of_refraction_label = tk.Label(popup_window41, text="Angle of refraction (degree): ", font=("Terakatal", 14),
                                         bg="#444654")
    angle_of_refraction_label.grid(row=1, column=0)
    angle_of_refraction_entry = tk.Entry(popup_window41, width=15, font="sans-serif")
    angle_of_refraction_entry.grid(row=1, column=1, padx=5, pady=5)

    refractive_index_of_second_medium_label = tk.Label(popup_window41, text="Refractive index of second medium: ",
                                                       font=("Terakatal", 14), bg="#444654")
    refractive_index_of_second_medium_label.grid(row=2, column=0)
    refractive_index_of_second_medium_entry = tk.Entry(popup_window41, width=15, font="sans-serif")
    refractive_index_of_second_medium_entry.grid(row=2, column=1, padx=5, pady=5)

    refractive_index_of_first_medium_label = tk.Label(popup_window41, text="Refractive index of first medium: ",
                                                      font=("Terakatal", 14), bg="#444654")
    refractive_index_of_first_medium_label.grid(row=3, column=0)
    refractive_index_of_first_medium_entry = tk.Entry(popup_window41, width=15, font="sans-serif")
    refractive_index_of_first_medium_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window41, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_angle_of_incidence(angle_of_refraction_entry,
                                                                              refractive_index_of_second_medium_entry,
                                                                              refractive_index_of_first_medium_entry,
                                                                              angle_of_incidence_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window41, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear41a(angle_of_refraction_entry,
                                                      refractive_index_of_second_medium_entry,
                                                      refractive_index_of_first_medium_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a label to display the Angle of incidence result.
    angle_of_incidence_label = tk.Label(popup_window41, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    angle_of_incidence_label.grid(row=5, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window41, width=685, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window41, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window41, height=6, width=68, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """SNELL's LAW:
             Snell's law, also known as the law of refraction, describes the bending 
of light as it passes from one medium to another with a different index of 
refraction. It states that the ratio of the sine of the angle of incidence to the 
sine of the angle of refraction is equal to the ratio of the indices of refraction of the two media."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window41, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window41, height=8, width=68, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Snell's Law is:
       sinθ1 / sinθ2 = n2 / n1

    where:
        θ1 = Angle of incidence
        θ1 = Angle of refraction
        n1 = Refractive index of first medium
        n2 = Refractive index of second medium"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window41.mainloop()


# Create Popup window for Critical Angle
def popup42():
    popup_window42 = tk.Toplevel(root, bg="#444654")
    popup_window42.title("Calculator")
    popup_window42.geometry("625x630")
    popup_window42.resizable(height=False, width=False)
    # Create Critical Angle layout
    # Create a label for Critical Angle
    label1 = tk.Label(popup_window42, text="Critical Angle", font=("Calbiri", 17, "bold"), padx=230, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Refractive index of second medium and Refractive index of first medium.
    refractive_index_of_second_medium_label = tk.Label(popup_window42, text="Refractive index of second medium : ",
                                                       font=("Terakatal", 14), bg="#444654")
    refractive_index_of_second_medium_label.grid(row=1, column=0)
    refractive_index_of_second_medium_entry = tk.Entry(popup_window42, width=15, font="sans-serif")
    refractive_index_of_second_medium_entry.grid(row=1, column=1, padx=5, pady=5)

    refractive_index_of_first_medium_label = tk.Label(popup_window42, text="Refractive index of first medium : ",
                                                      font=("Terakatal", 14), bg="#444654")
    refractive_index_of_first_medium_label.grid(row=2, column=0)
    refractive_index_of_first_medium_entry = tk.Entry(popup_window42, width=15, font="sans-serif")
    refractive_index_of_first_medium_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window42, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_critical_angle(refractive_index_of_second_medium_entry,
                                                                          refractive_index_of_first_medium_entry,
                                                                          critical_angle_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window42, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear42(refractive_index_of_second_medium_entry,
                                                     refractive_index_of_first_medium_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Critical angle result.
    critical_angle_label = tk.Label(popup_window42, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    critical_angle_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window42, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window42, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window42, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """CRITICAL ANGLE:
             The angle of incidence for which the angle of refraction is 90 
degrees is called as the critical angle."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window42, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window42, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Critical Angle is:
    sinθc = n2 / n1
    
    where:
       θc = Critical Angle
       n2 = Refractive index of second medium
       n1 = Refractive index of first medium"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window42.mainloop()


# Create Popup window for Image Location
def popup43():
    popup_window43 = tk.Toplevel(root, bg="#444654")
    popup_window43.title("Calculator")
    popup_window43.geometry("625x650")
    popup_window43.resizable(height=False, width=False)
    # Create Image Location layout
    # Create a label for Image Location
    label1 = tk.Label(popup_window43, text="Focal Length", font=("Calbiri", 17, "bold"), padx=230, pady=5, fg="#3A98B9",
                      bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Object distance and Image distance.
    object_distance_label = tk.Label(popup_window43, text="Object distance (m): ",
                                     font=("Terakatal", 14), bg="#444654")
    object_distance_label.grid(row=1, column=0)
    object_distance_entry = tk.Entry(popup_window43, width=15, font="sans-serif")
    object_distance_entry.grid(row=1, column=1, padx=5, pady=5)

    image_distance_label = tk.Label(popup_window43, text="Image distance (m): ",
                                    font=("Terakatal", 14), bg="#444654")
    image_distance_label.grid(row=2, column=0)
    image_distance_entry = tk.Entry(popup_window43, width=15, font="sans-serif")
    image_distance_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window43, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_focal_length(object_distance_entry,
                                                                        image_distance_entry,
                                                                        focal_length_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window43, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear43(object_distance_entry,
                                                     image_distance_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Focal length result.
    focal_length_label = tk.Label(popup_window43, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    focal_length_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window43, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window43, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window43, height=4, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """FOCAL LENGTH:
             The focal length ( f ) is the distance from a lens or mirror to the 
focal point. This is the distance from a lens or mirror at which parallel 
light rays will meet."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window43, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window43, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Focal Length is:
    1 / f = 1 / do + 1 / di

    where:
       f = Focal Length
      do = Object distance
      di = Image distance"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window43.mainloop()


# Create Popup window for Magnification
def popup44():
    popup_window44 = tk.Toplevel(root, bg="#444654")
    popup_window44.title("Calculator")
    popup_window44.geometry("625x610")
    popup_window44.resizable(height=False, width=False)
    # Create Magnification layout
    # Create a label for Magnification
    label1 = tk.Label(popup_window44, text="Magnification", font=("Calbiri", 17, "bold"), padx=220, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Object distance and Image distance.
    image_distance_label = tk.Label(popup_window44, text="Size of the Image (m): ",
                                    font=("Terakatal", 14), bg="#444654")
    image_distance_label.grid(row=1, column=0)
    image_distance_entry = tk.Entry(popup_window44, width=15, font="sans-serif")
    image_distance_entry.grid(row=1, column=1, padx=5, pady=5)

    object_distance_label = tk.Label(popup_window44, text="Size of the Object (m): ",
                                     font=("Terakatal", 14), bg="#444654")
    object_distance_label.grid(row=2, column=0)
    object_distance_entry = tk.Entry(popup_window44, width=15, font="sans-serif")
    object_distance_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window44, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_magnification(object_distance_entry,
                                                                         image_distance_entry,
                                                                         magnification_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window44, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear43(object_distance_entry,
                                                     image_distance_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Magnification result.
    magnification_label = tk.Label(popup_window44, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    magnification_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window44, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window44, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window44, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """MAGNIFICATION:
             Magnification is defined as the ratio of the size of the image to 
that of the object."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window44, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window44, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Magnification is:
       M = hi / ho

    where:
       M = Magnification
      hi = Size of the image
      ho = Size of the object """
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window44.mainloop()


# Create Popup window for Spherical Mirrors
def popup45():
    popup_window45 = tk.Toplevel(root, bg="#444654")
    popup_window45.title("Calculator")
    popup_window45.geometry("625x550")
    popup_window45.resizable(height=False, width=False)
    # Create Spherical Mirrors layout
    # Create a label for Spherical Mirrors.
    label1 = tk.Label(popup_window45, text="Spherical Mirrors", font=("Calbiri", 17, "bold"), padx=200, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries Radius of curvature.
    radius_of_curvature_label = tk.Label(popup_window45, text="Radius of curvature (m): ",
                                         font=("Terakatal", 14), bg="#444654")
    radius_of_curvature_label.grid(row=1, column=0)
    radius_of_curvature_entry = tk.Entry(popup_window45, width=15, font="sans-serif")
    radius_of_curvature_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window45, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_focal_length1(radius_of_curvature_entry,
                                                                         focal_length1_label))
    calculate_button.grid(row=2, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window45, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear40(radius_of_curvature_entry))
    clear_button.grid(row=2, column=0, padx=5, pady=5)

    # Create a label to display the Focal Length.
    focal_length1_label = tk.Label(popup_window45, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    focal_length1_label.grid(row=3, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window45, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=4, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window45, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=5, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window45, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """SPHERICAL MIRRORS:
             A mirror with a reflecting surface that seems to be the portion of a hollow glass sphere is called a spherical mirror."""
    T.grid(row=6, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window45, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window45, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Spherical Mirrors is:
       f = r / 2

    where:
       f = Focal length
       r = Radius of curvature"""
    T2.grid(row=8, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window45.mainloop()


# Electricity and Magnetism
# Create Popup window for Coulomb's Law
def popup46():
    popup_window46 = tk.Toplevel(root, bg="#444654")
    popup_window46.title("Calculator")
    popup_window46.geometry("625x760")
    popup_window46.resizable(height=False, width=False)
    # Create Coulomb's's Law layout
    # Create label for Coulomb's's Law
    label1 = tk.Label(popup_window46, text="Coulomb's's Law", font=("Calbiri", 17, "bold"), padx=210, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    # Create labels and entries for Charge q1, Charge q2 and Distance.
    charge_q1_label = tk.Label(popup_window46, text="Charge q1 (C): ", font=("Terakatal", 14), bg="#444654")
    charge_q1_label.grid(row=1, column=0)
    charge_q1_entry = tk.Entry(popup_window46, width=15, font="sans-serif")
    charge_q1_entry.grid(row=1, column=1, padx=5, pady=5)

    charge_q2_label = tk.Label(popup_window46, text="Charge q2 (C): ",
                               font=("Terakatal", 14), bg="#444654")
    charge_q2_label.grid(row=2, column=0)
    charge_q2_entry = tk.Entry(popup_window46, width=15, font="sans-serif")
    charge_q2_entry.grid(row=2, column=1, padx=5, pady=5)

    distance_label = tk.Label(popup_window46, text="Distance (m) : ",
                              font=("Terakatal", 14), bg="#444654")
    distance_label.grid(row=3, column=0)
    distance_entry = tk.Entry(popup_window46, width=15, font="sans-serif")
    distance_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window46, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_coulomb_force(charge_q1_entry,
                                                                         charge_q2_entry,
                                                                         distance_entry,
                                                                         coulomb_force_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window46, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear46(charge_q1_entry,
                                                     charge_q2_entry,
                                                     distance_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a label to display the Angle of incidence result.
    coulomb_force_label = tk.Label(popup_window46, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    coulomb_force_label.grid(row=5, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window46, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window46, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window46, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """COULOMB's LAW:
             According to Coulomb’s law, the force of attraction or repulsion 
between two charged bodies is directly proportional to the product of 
their charges and inversely proportional to the square of the distance 
between them. """
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window46, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window46, height=9, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Coulomb's Law is:
       F = k . q1.q2 / r²

    where:
       F = Coulomb's force
       k = Coulomb Constant
      q1 = Charge q1
      q2 = Charge q2 
       r = Distance"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window46.mainloop()


# Create Popup window for Electric Field
def popup47():
    popup_window47 = tk.Toplevel(root, bg="#444654")
    popup_window47.title("Calculator")
    popup_window47.geometry("625x590")
    popup_window47.resizable(height=False, width=False)
    # Create Electric Field layout
    # Create a label for Electric Field
    label1 = tk.Label(popup_window47, text="Electric Field", font=("Calbiri", 17, "bold"), padx=230, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Electrostatic force and Positive test charge.
    electrostatic_force_label = tk.Label(popup_window47, text="Electrostatic force (N): ",
                                         font=("Terakatal", 14), bg="#444654")
    electrostatic_force_label.grid(row=1, column=0)
    electrostatic_force_entry = tk.Entry(popup_window47, width=15, font="sans-serif")
    electrostatic_force_entry.grid(row=1, column=1, padx=5, pady=5)

    positive_test_charge_label = tk.Label(popup_window47, text="Positive test charge (C): ",
                                          font=("Terakatal", 14), bg="#444654")
    positive_test_charge_label.grid(row=2, column=0)
    positive_test_charge_entry = tk.Entry(popup_window47, width=15, font="sans-serif")
    positive_test_charge_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window47, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_electric_field(electrostatic_force_entry,
                                                                          positive_test_charge_entry,
                                                                          electric_field_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window47, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear47(electrostatic_force_entry, positive_test_charge_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Electric field result.
    electric_field_label = tk.Label(popup_window47, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    electric_field_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window47, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window47, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window47, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """ELECTRIC FIELD:
             Electric field can be defined as the region of space around an electrically charged particle or an object in which the charge body experiences force. """
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window47, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window47, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Electric Field is:
       E = F / q

    where:
       E = Electric field
       F = Electrostatic force
       q = Positive test charge"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window47.mainloop()


# Create Popup window for Electric Potential
def popup48():
    popup_window48 = tk.Toplevel(root, bg="#444654")
    popup_window48.title("Calculator")
    popup_window48.geometry("625x680")
    popup_window48.resizable(height=False, width=False)
    # Create Electric Potential layout
    # Create a label for Electric Potential
    label1 = tk.Label(popup_window48, text="Electric Potential", font=("Calbiri", 17, "bold"), padx=210, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Potential energy difference and Electric charge.
    potential_energy_difference_label = tk.Label(popup_window48, text="Potential energy difference (J): ",
                                                 font=("Terakatal", 14), bg="#444654")
    potential_energy_difference_label.grid(row=1, column=0)
    potential_energy_difference_entry = tk.Entry(popup_window48, width=15, font="sans-serif")
    potential_energy_difference_entry.grid(row=1, column=1, padx=5, pady=5)

    electric_charge_label = tk.Label(popup_window48, text="Electric charge (C): ",
                                     font=("Terakatal", 14), bg="#444654")
    electric_charge_label.grid(row=2, column=0)
    electric_charge_entry = tk.Entry(popup_window48, width=15, font="sans-serif")
    electric_charge_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window48, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_electric_potential(potential_energy_difference_entry,
                                                                              electric_charge_entry,
                                                                              electric_potential_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window48, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear48(potential_energy_difference_entry, electric_charge_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Electric potential result.
    electric_potential_label = tk.Label(popup_window48, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    electric_potential_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window48, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window48, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window48, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """ELECTRIC POTENTIAL:
                 Electric potential is a scalar physical quantity that is used to 
describe the electrical potential energy per unit charge at a point in 
space. It is also called the electric potential difference or voltage. Electric potential is the amount of work needed to move a unit positive charge 
from a reference point to a specific point in an electric field."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window48, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window48, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Electric Potential is:
       V =  k . Q / r

    where:
       V = Electric potential
       Q = Electric charge
       r = Distance"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window48.mainloop()


# Create Popup window for Capacitance
def popup49():
    popup_window49 = tk.Toplevel(root, bg="#444654")
    popup_window49.title("Calculator")
    popup_window49.geometry("625x630")
    popup_window49.resizable(height=False, width=False)
    # Create a Capacitance layout
    # Create a label for Capacitance
    label1 = tk.Label(popup_window49, text="Capacitance", font=("Calbiri", 17, "bold"), padx=230, pady=5, fg="#3A98B9",
                      bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Electric charge and Potential difference.

    electric_charge_label = tk.Label(popup_window49, text="Electric charge (C): ",
                                     font=("Terakatal", 14), bg="#444654")
    electric_charge_label.grid(row=1, column=0)
    electric_charge_entry = tk.Entry(popup_window49, width=15, font="sans-serif")
    electric_charge_entry.grid(row=1, column=1, padx=5, pady=5)

    potential_difference_label = tk.Label(popup_window49, text="Potential difference (V): ",
                                          font=("Terakatal", 14), bg="#444654")
    potential_difference_label.grid(row=2, column=0)
    potential_difference_entry = tk.Entry(popup_window49, width=15, font="sans-serif")
    potential_difference_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window49, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_capacitance(electric_charge_entry,
                                                                       potential_difference_entry,
                                                                       capacitance_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window49, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear49(electric_charge_entry, potential_difference_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Capacitance result.
    capacitance_label = tk.Label(popup_window49, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    capacitance_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window49, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window49, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window49, height=4, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """CAPACITANCE:
                 The Capacitance of a capacitor is defined as the ratio of the 
magnitude of the charge on either conductor to the potential difference between the conductors."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window49, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window49, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Capacitance is:
       C = Q / V

    where:
       C = Capacitance
       Q = Electric charge
       V = Electric potential"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window49.mainloop()


# Create Popup window for Parallel Plate Capacitor
def popup50():
    popup_window50 = tk.Toplevel(root, bg="#444654")
    popup_window50.title("Calculator")
    popup_window50.geometry("635x700")
    popup_window50.resizable(height=False, width=False)
    # Create a Parallel Plate Capacitor layout
    # Create label for Parallel Plate Capacitor
    label1 = tk.Label(popup_window50, text="Parallel Plate Capacitor", font=("Calbiri", 17, "bold"), padx=170, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    # Create labels and entries for Permittivity, Area and Separation distance.
    permittivity_label = tk.Label(popup_window50, text="Permittivity (F/m) : ", font=("Terakatal", 14), bg="#444654")
    permittivity_label.grid(row=1, column=0)
    permittivity_entry = tk.Entry(popup_window50, width=15, font="sans-serif")
    permittivity_entry.grid(row=1, column=1, padx=5, pady=5)

    area_label = tk.Label(popup_window50, text="Area (m²) : ",
                          font=("Terakatal", 14), bg="#444654")
    area_label.grid(row=2, column=0)
    area_entry = tk.Entry(popup_window50, width=15, font="sans-serif")
    area_entry.grid(row=2, column=1, padx=5, pady=5)

    separation_distance_label = tk.Label(popup_window50, text="Separation distance (m) : ",
                                         font=("Terakatal", 14), bg="#444654")
    separation_distance_label.grid(row=3, column=0)
    separation_distance_entry = tk.Entry(popup_window50, width=15, font="sans-serif")
    separation_distance_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window50, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_capacitance1(permittivity_entry,
                                                                        area_entry,
                                                                        separation_distance_entry,
                                                                        capacitance1_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window50, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear50(permittivity_entry,
                                                     area_entry,
                                                     separation_distance_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a label to display the Capacitance result.
    capacitance1_label = tk.Label(popup_window50, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    capacitance1_label.grid(row=5, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window50, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window50, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window50, height=4, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """PARALLEL PLATE CAPACITOR:
             When two parallel plates are connected across a battery, the plates are charged and an electric field is established between them, and this 
setup is known as the parallel plate capacitor."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window50, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window50, height=8, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Parallel Plate Capacitor is:
       C =  ϵ . A / S

    where:
       C = Capacitance
       ϵ = Permittivity
       A = Area
       S = Separation distance"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window50.mainloop()


# Create Popup window for Electric current
def popup51():
    popup_window51 = tk.Toplevel(root, bg="#444654")
    popup_window51.title("Calculator")
    popup_window51.geometry("645x630")
    popup_window51.resizable(height=False, width=False)
    # Create a Electric current layout
    # Create a label for Electric current
    label1 = tk.Label(popup_window51, text="Electric current", font=("Calbiri", 17, "bold"), padx=220, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Electric charge and Time.
    electric_charge_label = tk.Label(popup_window51, text="Electric charge (C): ",
                                     font=("Terakatal", 14), bg="#444654")
    electric_charge_label.grid(row=1, column=0)
    electric_charge_entry = tk.Entry(popup_window51, width=15, font="sans-serif")
    electric_charge_entry.grid(row=1, column=1, padx=5, pady=5)

    time_label = tk.Label(popup_window51, text="Time (s): ",
                          font=("Terakatal", 14), bg="#444654")
    time_label.grid(row=2, column=0)
    time_entry = tk.Entry(popup_window51, width=15, font="sans-serif")
    time_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window51, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_electric_current(electric_charge_entry,
                                                                            time_entry,
                                                                            electric_current_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window51, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear51(electric_charge_entry, time_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Electric current result.
    electric_current_label = tk.Label(popup_window51, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    electric_current_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window51, width=645, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window51, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window51, height=4, width=64, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """ELECTRIC CURRENT:
             Electric current is basically the flow or charge of the electric charge in motion in a conductor. It is said to exist when there is a net flow of 
charge through the region."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window51, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window51, height=7, width=64, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Electric current is:
       I = Q / t

    where:
       I = Electric current 
       Q = Electric charge
       t = Time"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window51.mainloop()


# Create Popup window for Ohm's Law
def popup52():
    popup_window52 = tk.Toplevel(root, bg="#444654")
    popup_window52.title("Calculator")
    popup_window52.geometry("625x620")
    popup_window52.resizable(height=False, width=False)
    # Create an Ohm's Law layout
    # Create a label for Ohm's Law
    label1 = tk.Label(popup_window52, text="Ohm's Law", font=("Calbiri", 17, "bold"), padx=230, pady=5, fg="#3A98B9",
                      bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Voltage and Resistance.
    voltage_label = tk.Label(popup_window52, text="Voltage (V): ",
                             font=("Terakatal", 14), bg="#444654")
    voltage_label.grid(row=1, column=0)
    voltage_entry = tk.Entry(popup_window52, width=15, font="sans-serif")
    voltage_entry.grid(row=1, column=1, padx=5, pady=5)

    resistance_label = tk.Label(popup_window52, text="Resistance (Ω): ",
                                font=("Terakatal", 14), bg="#444654")
    resistance_label.grid(row=2, column=0)
    resistance_entry = tk.Entry(popup_window52, width=15, font="sans-serif")
    resistance_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window52, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_current(voltage_entry,
                                                                   resistance_entry,
                                                                   current_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window52, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear52(voltage_entry, resistance_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Current result.
    current_label = tk.Label(popup_window52, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    current_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window52, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window52, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window52, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """OHM's LAW:
             Ohm’s law states that the current through a conductor between 
two points is directly proportional to the voltage across the two points."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window52, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window52, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Ohm's Law is:
       I = V / R

    where:
       I = Current 
       V = Voltage
       R = Resistance"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window52.mainloop()


# Create Popup window for Electric Resistance
def popup53():
    popup_window53 = tk.Toplevel(root, bg="#444654")
    popup_window53.title("Calculator")
    popup_window53.geometry("615x720")
    popup_window53.resizable(height=False, width=False)
    # Create a Electric Resistance layout
    # Create label for Electric Resistance
    label1 = tk.Label(popup_window53, text="Electric Resistance", font=("Calbiri", 17, "bold"), padx=190, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Electrical resistivity, Length of the conductor and Cross-section.
    electrical_resistivity_label = tk.Label(popup_window53, text="Electrical resistivity (Ω/m) : ",
                                            font=("Terakatal", 14), bg="#444654")
    electrical_resistivity_label.grid(row=1, column=0)
    electrical_resistivity_entry = tk.Entry(popup_window53, width=15, font="sans-serif")
    electrical_resistivity_entry.grid(row=1, column=1, padx=5, pady=5)

    length_of_the_conductor_label = tk.Label(popup_window53, text="Length of the conductor (m) : ",
                                             font=("Terakatal", 14), bg="#444654")
    length_of_the_conductor_label.grid(row=2, column=0, padx=5, pady=5)
    length_of_the_conductor_entry = tk.Entry(popup_window53, width=15, font="sans-serif")
    length_of_the_conductor_entry.grid(row=2, column=1, padx=5, pady=5)

    cross_section_label = tk.Label(popup_window53, text="Cross-section (m²) : ",
                                   font=("Terakatal", 14), bg="#444654")
    cross_section_label.grid(row=3, column=0)
    cross_section_entry = tk.Entry(popup_window53, width=15, font="sans-serif")
    cross_section_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window53, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_resistance(electrical_resistivity_entry,
                                                                      length_of_the_conductor_entry,
                                                                      cross_section_entry,
                                                                      resistance_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window53, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear53(electrical_resistivity_entry,
                                                     length_of_the_conductor_entry,
                                                     cross_section_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a label to display the Resistance result.
    resistance_label = tk.Label(popup_window53, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    resistance_label.grid(row=5, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window53, width=615, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window53, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window53, height=5, width=61, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """ELECTRIC RESISTANCE:
             Electric resistance is the measure of an electrical component's 
opposition to the flow of electric current through it. It is defined as the 
ratio of the voltage applied across a conductor to the current flowing 
through the conductor."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window53, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window53, height=8, width=61, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Electric Resistance is:
       R =  ρ . l / A

    where:
       R = Resistance
       ρ  = Electrical resistivity 
       l = Length of the conductor 
       A = Cross section"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window53.mainloop()


# Create Popup window for Resistors in Series
def popup54():
    popup_window54 = tk.Toplevel(root, bg="#444654")
    popup_window54.title("Calculator")
    popup_window54.geometry("635x650")
    popup_window54.resizable(height=False, width=False)
    # Create a Resistors in Series layout
    # Create a label for Resistors in Series
    label1 = tk.Label(popup_window54, text="Resistors in Series", font=("Calbiri", 17, "bold"), padx=210, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Resistance1 and Resistance2.
    resistance1_label = tk.Label(popup_window54, text="Resistance R1 (Ω): ",
                                 font=("Terakatal", 14), bg="#444654")
    resistance1_label.grid(row=1, column=0)
    resistance1_entry = tk.Entry(popup_window54, width=15, font="sans-serif")
    resistance1_entry.grid(row=1, column=1, padx=5, pady=5)

    resistance2_label = tk.Label(popup_window54, text="Resistance R2 (Ω): ",
                                 font=("Terakatal", 14), bg="#444654")
    resistance2_label.grid(row=2, column=0)
    resistance2_entry = tk.Entry(popup_window54, width=15, font="sans-serif")
    resistance2_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window54, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_total_resistance(resistance1_entry,
                                                                            resistance2_entry,
                                                                            total_resistance_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window54, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear54(resistance1_entry, resistance2_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Total resistance result.
    total_resistance_label = tk.Label(popup_window54, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    total_resistance_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window54, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window54, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window54, height=5, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """RESISTORS IN SERIES:
             Resistors in series are two or more resistors connected end-to-end such that the same current flows through each resistor in the circuit. The 
total resistance of resistors in series is the sum of the individual resistance"""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window54, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window54, height=7, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Resistors in Series is:
       R = R1 + R2

    where:
       R = Total Resistance
      R1 = Resistance
      R2 = Resistance"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window54.mainloop()


# Create Popup window for Resistors in Parallel
def popup55():
    popup_window55 = tk.Toplevel(root, bg="#444654")
    popup_window55.title("Calculator")
    popup_window55.geometry("625x650")
    popup_window55.resizable(height=False, width=False)
    # Create a Resistors in Parallel layout
    # Create a label for Resistors in Parallel
    label1 = tk.Label(popup_window55, text="Resistors in Parallel", font=("Calbiri", 17, "bold"), padx=190, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Resistance1 and Resistance2.
    resistance1_label = tk.Label(popup_window55, text="Resistance R1 (Ω): ",
                                 font=("Terakatal", 14), bg="#444654")
    resistance1_label.grid(row=1, column=0)
    resistance1_entry = tk.Entry(popup_window55, width=15, font="sans-serif")
    resistance1_entry.grid(row=1, column=1, padx=5, pady=5)

    resistance2_label = tk.Label(popup_window55, text="Resistance R2 (Ω): ",
                                 font=("Terakatal", 14), bg="#444654")
    resistance2_label.grid(row=2, column=0)
    resistance2_entry = tk.Entry(popup_window55, width=15, font="sans-serif")
    resistance2_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window55, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_total_resistance1(resistance1_entry,
                                                                             resistance2_entry,
                                                                             total_resistance1_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window55, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear55(resistance1_entry, resistance2_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Total resistance result.
    total_resistance1_label = tk.Label(popup_window55, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    total_resistance1_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window55, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window55, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window55, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """RESISTORS IN PARALLEL:
             Resistors in parallel are two or more resistors connected across 
each other with both ends of all resistors connected together to form a 
junction. The total resistance of resistors in parallel is less than the value of the smallest individual resistance."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window55, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window55, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Resistors in Parallel is:
    1 / R = 1 / R1 + 1 / R2

    where:
        R = Total Resistance
       R1 = Resistance
       R2 = Resistance"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window55.mainloop()


# Create Popup window for Capacitors in Series
def popup56():
    popup_window56 = tk.Toplevel(root, bg="#444654")
    popup_window56.title("Calculator")
    popup_window56.geometry("625x700")
    popup_window56.resizable(height=False, width=False)
    # Create a Capacitors in Series layout
    # Create a label Capacitors in Series
    label1 = tk.Label(popup_window56, text="Capacitors in Series", font=("Calbiri", 17, "bold"), padx=190, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Capacitance and Capacitance2.
    capacitance1_label = tk.Label(popup_window56, text="capacitance C1 (F): ",
                                  font=("Terakatal", 14), bg="#444654")
    capacitance1_label.grid(row=1, column=0)
    capacitance1_entry = tk.Entry(popup_window56, width=15, font="sans-serif")
    capacitance1_entry.grid(row=1, column=1, padx=5, pady=5)

    capacitance2_label = tk.Label(popup_window56, text="capacitance C2 (F): ",
                                  font=("Terakatal", 14), bg="#444654")
    capacitance2_label.grid(row=2, column=0)
    capacitance2_entry = tk.Entry(popup_window56, width=15, font="sans-serif")
    capacitance2_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window56, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_total_capacitance(capacitance1_entry,
                                                                             capacitance2_entry,
                                                                             total_capacitance1_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window56, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear56(capacitance1_entry, capacitance2_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Total capacitance result.
    total_capacitance1_label = tk.Label(popup_window56, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    total_capacitance1_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window56, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window56, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window56, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """CAPACITORS IN SERIES:
             Capacitors in series are two or more capacitors connected end-to
-end such that the same charge is shared between them. In other words, 
the capacitors are connected in a single path so that the charge flows 
through one capacitor before flowing through the next. The total 
capacitance of capacitors in series is less than the value of the smallest 
individual capacitance."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window56, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window56, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Capacitors in Series is:
    1 / C = 1 / C1 + 1 / C2

    where:
        C = Total Capacitance
       C1 = Capacitance
       C2 = Capacitance"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window56.mainloop()


# Create Popup window for Capacitors in Parallel
def popup57():
    popup_window57 = tk.Toplevel(root, bg="#444654")
    popup_window57.title("Calculator")
    popup_window57.geometry("635x710")
    popup_window57.resizable(height=False, width=False)
    # Create a Capacitors in Parallel layout
    # Create a label Capacitors in Parallel
    label1 = tk.Label(popup_window57, text="Capacitors in Parallel", font=("Calbiri", 17, "bold"), padx=170, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Capacitance1 and Capacitance2.
    capacitance1_label = tk.Label(popup_window57, text="Capacitance C1 (F): ",
                                  font=("Terakatal", 14), bg="#444654")
    capacitance1_label.grid(row=1, column=0)
    capacitance1_entry = tk.Entry(popup_window57, width=15, font="sans-serif")
    capacitance1_entry.grid(row=1, column=1, padx=5, pady=5)

    capacitance2_label = tk.Label(popup_window57, text="Capacitance C2 (F): ",
                                  font=("Terakatal", 14), bg="#444654")
    capacitance2_label.grid(row=2, column=0)
    capacitance2_entry = tk.Entry(popup_window57, width=15, font="sans-serif")
    capacitance2_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window57, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_total_capacitance1(capacitance1_entry,
                                                                              capacitance2_entry,
                                                                              total_capacitance_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window57, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear57(capacitance1_entry, capacitance2_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Total capacitance result.
    total_capacitance_label = tk.Label(popup_window57, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    total_capacitance_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window57, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window57, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window57, height=7, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """CAPACITORS IN PARALLEL:
             Capacitors in parallel are two or more capacitors connected across 
each other with both ends of all capacitors connected together to form a 
junction. In other words, the capacitors are connected in a way that there 
are multiple paths for the charge to flow through the circuit. The total 
capacitance of capacitors in parallel is the sum of the individual 
capacitance. """
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window57, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window57, height=7, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Capacitors in Parallel is:
       C = C1 + C2

    where:
       C = Total Capacitance
      C1 = Capacitance
      C2 = Capacitance"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window57.mainloop()


# Create Popup window for Magnetic Force(Charge)
def popup58():
    popup_window58 = tk.Toplevel(root, bg="#444654")
    popup_window58.title("Calculator")
    popup_window58.geometry("625x750")
    popup_window58.resizable(height=False, width=False)
    # Create a Magnetic Force(Charge) layout
    # Create label for Magnetic Force(Charge)
    label1 = tk.Label(popup_window58, text="Magnetic Force(Charge)", font=("Calbiri", 17, "bold"), padx=170, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Particle charge, Velocity of particle, Magnetic field and Angle.
    particle_charge_label = tk.Label(popup_window58, text="Particle charge (C) : ",
                                     font=("Terakatal", 14), bg="#444654")
    particle_charge_label.grid(row=1, column=0)
    particle_charge_entry = tk.Entry(popup_window58, width=15, font="sans-serif")
    particle_charge_entry.grid(row=1, column=1, padx=5, pady=5)

    velocity_of_particle_label = tk.Label(popup_window58, text="Velocity of particle (m/s) : ",
                                          font=("Terakatal", 14), bg="#444654")
    velocity_of_particle_label.grid(row=2, column=0)
    velocity_of_particle_entry = tk.Entry(popup_window58, width=15, font="sans-serif")
    velocity_of_particle_entry.grid(row=2, column=1, padx=5, pady=5)

    magnetic_field_label = tk.Label(popup_window58, text="Magnetic field (T) : ",
                                    font=("Terakatal", 14), bg="#444654")
    magnetic_field_label.grid(row=3, column=0)
    magnetic_field_entry = tk.Entry(popup_window58, width=15, font="sans-serif")
    magnetic_field_entry.grid(row=3, column=1, padx=5, pady=5)

    angle_label = tk.Label(popup_window58, text="Angle (degree) : ",
                           font=("Terakatal", 14), bg="#444654")
    angle_label.grid(row=4, column=0, padx=5, pady=5)
    angle_entry = tk.Entry(popup_window58, width=15, font="sans-serif")
    angle_entry.grid(row=4, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window58, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_magnetic_force(particle_charge_entry,
                                                                          velocity_of_particle_entry,
                                                                          magnetic_field_entry, angle_entry,
                                                                          magnetic_force_label))
    calculate_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window58, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear58(particle_charge_entry, velocity_of_particle_entry,
                                                     magnetic_field_entry, angle_entry))
    clear_button.grid(row=5, column=0, padx=5, pady=5)

    # Create a label to display the Magnetic Force result.
    magnetic_force_label = tk.Label(popup_window58, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    magnetic_force_label.grid(row=6, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window58, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=7, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window58, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window58, height=4, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """MAGNETIC FORCE(charge):       
             The magnetic force is the force exerted by a magnetic field on a moving electric charge. It is perpendicular to both the velocity of the 
charge and the magnetic field."""
    T.grid(row=9, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window58, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=10, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window58, height=9, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Magnetic Force is:
       F = q.v.B.sinθ 
    
    where:
       F = Magnetic Force
       q = Particle charge
       v = Velocity of particle
       B = Magnetic field
       θ = Angle"""
    T2.grid(row=11, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window58.mainloop()


# Create Popup window for Magnetic Force(Current)
def popup59():
    popup_window59 = tk.Toplevel(root, bg="#444654")
    popup_window59.title("Calculator")
    popup_window59.geometry("635x800")
    popup_window59.resizable(height=False, width=False)
    # Create a Magnetic Force(Current) layout
    # Create label for Magnetic Force(Current)
    label1 = tk.Label(popup_window59, text="Magnetic Force(Current)", font=("Calbiri", 17, "bold"), padx=170, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Current, Length, Magnetic field and Angle.
    current_label = tk.Label(popup_window59, text="Current (A) : ",
                             font=("Terakatal", 14), bg="#444654")
    current_label.grid(row=1, column=0)
    current_entry = tk.Entry(popup_window59, width=15, font="sans-serif")
    current_entry.grid(row=1, column=1, padx=5, pady=5)

    length_label = tk.Label(popup_window59, text="Length (m) : ",
                            font=("Terakatal", 14), bg="#444654")
    length_label.grid(row=2, column=0)
    length_entry = tk.Entry(popup_window59, width=15, font="sans-serif")
    length_entry.grid(row=2, column=1, padx=5, pady=5)

    magnetic_field_label = tk.Label(popup_window59, text="Magnetic field (T) : ",
                                    font=("Terakatal", 14), bg="#444654")
    magnetic_field_label.grid(row=3, column=0)
    magnetic_field_entry = tk.Entry(popup_window59, width=15, font="sans-serif")
    magnetic_field_entry.grid(row=3, column=1, padx=5, pady=5)

    angle_label = tk.Label(popup_window59, text="Angle (degree) : ",
                           font=("Terakatal", 14), bg="#444654")
    angle_label.grid(row=4, column=0)
    angle_entry = tk.Entry(popup_window59, width=15, font="sans-serif")
    angle_entry.grid(row=4, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window59, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_magnetic_force0(current_entry, length_entry,
                                                                           magnetic_field_entry, angle_entry,
                                                                           magnetic_force1_label))
    calculate_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window59, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear59(current_entry, length_entry,
                                                     magnetic_field_entry, angle_entry))
    clear_button.grid(row=5, column=0, padx=5, pady=5)

    # Create a label to display the Magnetic Force result.
    magnetic_force1_label = tk.Label(popup_window59, fg="blue", font=("Verdana", 14), bg="#444654")
    magnetic_force1_label.grid(row=6, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window59, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=7, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window59, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window59, height=6, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """MAGNETIC FORCE(current):       
               The magnetic force in current-carrying conductors is the force 
experienced by a current-carrying conductor in a magnetic field. When an 
electric current flows through a conductor, it generates a magnetic field 
around the conductor. This magnetic field interacts with the external 
magnetic field, resulting in a force on the conductor."""
    T.grid(row=9, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window59, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=10, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window59, height=9, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Magnetic Force is:
       F = I.l.B.sinθ 

    where:
       F = Magnetic Force
       I = Current
       l = Length
       B = Magnetic field
       θ = Angle"""
    T2.grid(row=11, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window59.mainloop()


# Create Popup window for Biot-Savart Law
def popup60():
    popup_window60 = tk.Toplevel(root, bg="#444654")
    popup_window60.title("Calculator")
    popup_window60.geometry("635x820")
    popup_window60.resizable(height=False, width=False)
    # Create a Biot-Savart Law layout
    # Create label for Biot-Savart Law
    label1 = tk.Label(popup_window60, text="Biot-Savart Law", font=("Calbiri", 17, "bold"), padx=210, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Current, Length, Angle and Distance.
    current_label = tk.Label(popup_window60, text="Current (A) : ",
                             font=("Terakatal", 14), bg="#444654")
    current_label.grid(row=1, column=0)
    current_entry = tk.Entry(popup_window60, width=15, font="sans-serif")
    current_entry.grid(row=1, column=1, padx=5, pady=5)

    length_label = tk.Label(popup_window60, text="Length (m) : ",
                            font=("Terakatal", 14), bg="#444654")
    length_label.grid(row=2, column=0)
    length_entry = tk.Entry(popup_window60, width=15, font="sans-serif")
    length_entry.grid(row=2, column=1, padx=5, pady=5)

    angle_label = tk.Label(popup_window60, text="Angle (degree) : ",
                           font=("Terakatal", 14), bg="#444654")
    angle_label.grid(row=3, column=0)
    angle_entry = tk.Entry(popup_window60, width=15, font="sans-serif")
    angle_entry.grid(row=3, column=1, padx=5, pady=5)

    distance_label = tk.Label(popup_window60, text="Magnetic field (T) : ",
                              font=("Terakatal", 14), bg="#444654")
    distance_label.grid(row=4, column=0)
    distance_entry = tk.Entry(popup_window60, width=15, font="sans-serif")
    distance_entry.grid(row=4, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window60, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_magnetic_field(current_entry,
                                                                          length_entry, angle_entry,
                                                                          distance_entry,
                                                                          magnetic_field_label))
    calculate_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window60, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear60(current_entry, length_entry, angle_entry,
                                                     distance_entry))
    clear_button.grid(row=5, column=0, padx=5, pady=5)

    # Create a label to display the Magnetic Field result.
    magnetic_field_label = tk.Label(popup_window60, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    magnetic_field_label.grid(row=6, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window60, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=7, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window60, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window60, height=6, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """BIOT-SAVART LAW:       
             The Biot-Savart Law states that the magnetic field d B at a point P, 
produced by a small element of current I d l at a point Q, is proportional 
to the product of the current and the length of the element, and inversely 
proportional to the square of the distance between the point P and the 
point Q. """
    T.grid(row=9, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window60, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=10, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window60, height=10, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Biot-Savart Law is:
       B = (μ₀/4π) . (I . dl . sinθ) / r² 

    where:
       B = Magnetic field
       I = Current
      dl = Length
       θ = Angle
      μ₀ = Magnetic Constant
       r = Distance"""
    T2.grid(row=11, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window60.mainloop()


# Create Popup window for Solenoid
def popup61():
    popup_window61 = tk.Toplevel(root, bg="#444654")
    popup_window61.title("Calculator")
    popup_window61.geometry("625x750")
    popup_window61.resizable(height=False, width=False)
    # Create a Solenoid layout
    # Create label for Solenoid
    label1 = tk.Label(popup_window61, text="Solenoid", font=("Calbiri", 17, "bold"), padx=250, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    # Create labels and entries for Number of loops, Current and Length of the solenoid.
    number_of_loops_label = tk.Label(popup_window61, text="Number of loops : ",
                                     font=("Terakatal", 14), bg="#444654")
    number_of_loops_label.grid(row=1, column=0)
    number_of_loops_entry = tk.Entry(popup_window61, width=15, font="sans-serif")
    number_of_loops_entry.grid(row=1, column=1, padx=5, pady=5)

    current_label = tk.Label(popup_window61, text="Current (A) : ",
                             font=("Terakatal", 14), bg="#444654")
    current_label.grid(row=2, column=0)
    current_entry = tk.Entry(popup_window61, width=15, font="sans-serif")
    current_entry.grid(row=2, column=1, padx=5, pady=5)

    length_of_the_solenoid_label = tk.Label(popup_window61, text="Length of the solenoid (m) : ",
                                            font=("Terakatal", 14), bg="#444654")
    length_of_the_solenoid_label.grid(row=3, column=0)
    length_of_the_solenoid_entry = tk.Entry(popup_window61, width=15, font="sans-serif")
    length_of_the_solenoid_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window61, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_magnetic_field0(number_of_loops_entry,
                                                                           current_entry,
                                                                           length_of_the_solenoid_entry,
                                                                           magnetic_field1_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window61, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear61(number_of_loops_entry,
                                                     current_entry,
                                                     length_of_the_solenoid_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a label to display the Magnetic field result.
    magnetic_field1_label = tk.Label(popup_window61, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    magnetic_field1_label.grid(row=5, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window61, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window61, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window61, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """SOLENOID:       
               A solenoid is an electromagnetic device that converts electrical 
energy into mechanical motion or force by producing a magnetic field 
when a current is passed through a coil of wire. It typically consists of a 
cylindrical coil of wire, with a ferromagnetic core inside, that produces a 
uniform magnetic field in the central region of the coil."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window61, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window61, height=8, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for magnetic field produced by a Solenoid is:
       B = μ₀.N.I / l 

    where:
       B = Magnetic field
       N = Number of loops
       I = Current
       l = Length of the solenoid"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window61.mainloop()


# Create Popup window for Straight Wire
def popup62():
    popup_window62 = tk.Toplevel(root, bg="#444654")
    popup_window62.title("Calculator")
    popup_window62.geometry("625x680")
    popup_window62.resizable(height=False, width=False)
    # Create a Straight Wire layout
    # Create a label Straight Wire
    label1 = tk.Label(popup_window62, text="Straight Wire", font=("Calbiri", 17, "bold"), padx=230, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Electric current and Distance from the wire.
    electric_current_label = tk.Label(popup_window62, text="Electric current (A): ",
                                      font=("Terakatal", 14), bg="#444654")
    electric_current_label.grid(row=1, column=0)
    electric_current_entry = tk.Entry(popup_window62, width=15, font="sans-serif")
    electric_current_entry.grid(row=1, column=1, padx=5, pady=5)

    distance_from_the_wire_label = tk.Label(popup_window62, text="Distance from the wire (m): ",
                                            font=("Terakatal", 14), bg="#444654")
    distance_from_the_wire_label.grid(row=2, column=0)
    distance_from_the_wire_entry = tk.Entry(popup_window62, width=15, font="sans-serif")
    distance_from_the_wire_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window62, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_magnetic_field1(electric_current_entry,
                                                                           distance_from_the_wire_entry,
                                                                           magnetic_field_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window62, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear62(electric_current_entry, distance_from_the_wire_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Magnetic field result.
    magnetic_field_label = tk.Label(popup_window62, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    magnetic_field_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window62, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window62, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window62, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """STRAIGHT WIRE:       
             A straight wire is a conductor in the shape of a straight line, 
through which an electric current flows. The magnetic field produced by 
a straight wire can be calculated using the Biot-Savart Law, which 
describes the magnetic field produced by a steady current in a wire."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window62, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window62, height=8, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for magnetic field produced by a Straight Wire is:
       B = μ₀/4π . 2.I / r 

    where:
       B = Magnetic field
       I = Electric Current
       r = Distance from the wire
       μ₀ = Magnetic Constant"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window62.mainloop()


# Create Popup window for Parallel Wire
def popup63():
    popup_window63 = tk.Toplevel(root, bg="#444654")
    popup_window63.title("Calculator")
    popup_window63.geometry("635x720")
    popup_window63.resizable(height=False, width=False)
    # Create a Parallel Wire layout
    # Create label for Parallel Wire
    label1 = tk.Label(popup_window63, text="Parallel Wire", font=("Calbiri", 17, "bold"), padx=230, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Current of the wire 1, Current of the wire 2 and Distance from the wire.
    current_of_the_wire1_label = tk.Label(popup_window63, text="Current of the wire 1 (A) : ",
                                          font=("Terakatal", 14), bg="#444654")
    current_of_the_wire1_label.grid(row=1, column=0)
    current_of_the_wire1_entry = tk.Entry(popup_window63, width=15, font="sans-serif")
    current_of_the_wire1_entry.grid(row=1, column=1, padx=5, pady=5)

    current_of_the_wire2_label = tk.Label(popup_window63, text="Current of the wire 2 (A) : ",
                                          font=("Terakatal", 14), bg="#444654")
    current_of_the_wire2_label.grid(row=2, column=0)
    current_of_the_wire2_entry = tk.Entry(popup_window63, width=15, font="sans-serif")
    current_of_the_wire2_entry.grid(row=2, column=1, padx=5, pady=5)

    distance_from_the_wire_label = tk.Label(popup_window63, text="Distance from the wire (m) : ",
                                            font=("Terakatal", 14), bg="#444654")
    distance_from_the_wire_label.grid(row=3, column=0)
    distance_from_the_wire_entry = tk.Entry(popup_window63, width=15, font="sans-serif")
    distance_from_the_wire_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window63, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_magnetic_force1(current_of_the_wire1_entry,
                                                                           current_of_the_wire2_entry,
                                                                           distance_from_the_wire_entry,
                                                                           magnetic_force_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window63, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear63(current_of_the_wire1_entry,
                                                     current_of_the_wire2_entry,
                                                     distance_from_the_wire_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a label to display the Magnetic force result.
    magnetic_force_label = tk.Label(popup_window63, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    magnetic_force_label.grid(row=5, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window63, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window63, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window63, height=5, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """PARALLEL WIRE:       
             Parallel wires are two or more conductive wires that run parallel to each other, with a fixed distance between them. When electrical current 
flows through parallel wires in the same direction, they produce a 
magnetic field that interacts with each other."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window63, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window63, height=8, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for magnetic field produced by a Parallel Wire is:
      Fm = μ₀.I1.I2 / 2π.r

    where:
      Fm = Magnetic force
      I1 = Current of the wire 1
      I2 = Current of the wire 2
       r = Distance from the wire"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window63.mainloop()


# Create Popup window for Electric Flux
def popup64():
    popup_window64 = tk.Toplevel(root, bg="#444654")
    popup_window64.title("Calculator")
    popup_window64.geometry("635x700")
    popup_window64.resizable(height=False, width=False)
    # Create a Electric Flux layout
    # Create label for Electric Flux
    label1 = tk.Label(popup_window64, text="Electric Flux", font=("Calbiri", 17, "bold"), padx=230, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Electric field, Surface area and Angle between E and A.
    electric_field_label = tk.Label(popup_window64, text="Electric field (V/m) : ",
                                    font=("Terakatal", 14), bg="#444654")
    electric_field_label.grid(row=1, column=0)
    electric_field_entry = tk.Entry(popup_window64, width=15, font="sans-serif")
    electric_field_entry.grid(row=1, column=1, padx=5, pady=5)

    surface_area_label = tk.Label(popup_window64, text="Surface area (m²) : ",
                                  font=("Terakatal", 14), bg="#444654")
    surface_area_label.grid(row=2, column=0)
    surface_area_entry = tk.Entry(popup_window64, width=15, font="sans-serif")
    surface_area_entry.grid(row=2, column=1, padx=5, pady=5)

    angle_between_E_and_A_label = tk.Label(popup_window64, text="Angle between E and A (degree) : ",
                                           font=("Terakatal", 14), bg="#444654")
    angle_between_E_and_A_label.grid(row=3, column=0)
    angle_between_E_and_A_entry = tk.Entry(popup_window64, width=15, font="sans-serif")
    angle_between_E_and_A_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window64, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_electric_flux(electric_field_entry,
                                                                         surface_area_entry,
                                                                         angle_between_E_and_A_entry,
                                                                         electric_flux_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window64, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear64(electric_field_entry,
                                                     surface_area_entry,
                                                     angle_between_E_and_A_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a label to display the Electric flux result.
    electric_flux_label = tk.Label(popup_window64, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    electric_flux_label.grid(row=5, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window64, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window64, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window64, height=4, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """ELECTRIC FLUX:       
             Electric flux is the measure of flow of the electric field through a 
given area. Electric flux is proportional to the number of electric field lines 
going through a normally perpendicular surface."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window64, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window64, height=8, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Electric Flux is:
      ΦE = E.A.cosθ

    where:
       Φ = Electric flux
       E = Electric field
       A = Surface area
       θ = Angle between E and Perpendicular A"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window64.mainloop()


# Create Popup window for Magnetic Flux
def popup65():
    popup_window65 = tk.Toplevel(root, bg="#444654")
    popup_window65.title("Calculator")
    popup_window65.geometry("615x680")
    popup_window65.resizable(height=False, width=False)
    # Create a Magnetic Flux layout
    # Create label for Magnetic Flux
    label1 = tk.Label(popup_window65, text="Magnetic Flux", font=("Calbiri", 17, "bold"), padx=220, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Magnetic field, Area and Angle between B and A.
    magnetic_field_label = tk.Label(popup_window65, text="Magnetic field (T) : ",
                                    font=("Terakatal", 14), bg="#444654")
    magnetic_field_label.grid(row=1, column=0)
    magnetic_field_entry = tk.Entry(popup_window65, width=15, font="sans-serif")
    magnetic_field_entry.grid(row=1, column=1, padx=5, pady=5)

    area_label = tk.Label(popup_window65, text="Area (m²) : ",
                          font=("Terakatal", 14), bg="#444654")
    area_label.grid(row=2, column=0)
    area_entry = tk.Entry(popup_window65, width=15, font="sans-serif")
    area_entry.grid(row=2, column=1, padx=5, pady=5)

    angle_between_B_and_A_label = tk.Label(popup_window65, text="Angle between E and A (degree) : ",
                                           font=("Terakatal", 14), bg="#444654")
    angle_between_B_and_A_label.grid(row=3, column=0)
    angle_between_B_and_A_entry = tk.Entry(popup_window65, width=15, font="sans-serif")
    angle_between_B_and_A_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window65, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_magnetic_flux(magnetic_field_entry,
                                                                         area_entry,
                                                                         angle_between_B_and_A_entry,
                                                                         magnetic_flux_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window65, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear65(magnetic_field_entry,
                                                     area_entry,
                                                     angle_between_B_and_A_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a label to display the Magnetic flux result.
    magnetic_flux_label = tk.Label(popup_window65, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    magnetic_flux_label.grid(row=5, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window65, width=615, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window65, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window65, height=4, width=61, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """MAGNETIC FLUX:       
                  The number of magnetic field lines flowing through a closed 
surface is known as magnetic flux. It calculates the total magnetic field 
that travels across a specific surface area."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window65, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window65, height=8, width=61, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Magnetic Flux is:
      ΦB = B.A.cosθ

    where:
      ΦB = Magnetic flux
       B = Magnetic field
       A = Surface area
       θ = Angle between E and Perpendicular A"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window65.mainloop()


# Create Popup window for Motional Emf
def popup66():
    popup_window66 = tk.Toplevel(root, bg="#444654")
    popup_window66.title("Calculator")
    popup_window66.geometry("605x680")
    popup_window66.resizable(height=False, width=False)
    # Create a Motional Emf layout
    # Create label for Motional Emf
    label1 = tk.Label(popup_window66, text="Motional Emf", font=("Calbiri", 17, "bold"), padx=210, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Magnetic field, Length and Velocity.
    magnetic_field_label = tk.Label(popup_window66, text="Magnetic field (T) : ",
                                    font=("Terakatal", 14), bg="#444654")
    magnetic_field_label.grid(row=1, column=0)
    magnetic_field_entry = tk.Entry(popup_window66, width=15, font="sans-serif")
    magnetic_field_entry.grid(row=1, column=1, padx=5, pady=5)

    length_label = tk.Label(popup_window66, text="Length (m) : ",
                            font=("Terakatal", 14), bg="#444654")
    length_label.grid(row=2, column=0)
    length_entry = tk.Entry(popup_window66, width=15, font="sans-serif")
    length_entry.grid(row=2, column=1, padx=5, pady=5)

    velocity_label = tk.Label(popup_window66, text="Velocity (m/s) : ",
                              font=("Terakatal", 14), bg="#444654")
    velocity_label.grid(row=3, column=0)
    velocity_entry = tk.Entry(popup_window66, width=15, font="sans-serif")
    velocity_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a calculate and clear button .
    calculate_button = tk.Button(popup_window66, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_motional_emf(magnetic_field_entry,
                                                                        length_entry,
                                                                        velocity_entry,
                                                                        motional_emf_label))
    calculate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(popup_window66, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear66(magnetic_field_entry,
                                                     length_entry,
                                                     velocity_entry))
    clear_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a label to display the Motional Emf result.
    motional_emf_label = tk.Label(popup_window66, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    motional_emf_label.grid(row=5, column=1, padx=5, pady=5)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window66, width=605, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window66, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window66, height=3, width=60, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """MOTIONAL EMF:       
             Motional emf is a process in which an emf is inserted into a 
conductor as a result of its movement within a magnetic field."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window66, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window66, height=8, width=60, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Motional Emf is:
       ε = B.l.v

    where:
       ε = Motional Emf
       B = Magnetic field
       l = Length
       v = Velocity"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window66.mainloop()


# Create Popup window for Induced Emf
def popup67():
    popup_window67 = tk.Toplevel(root, bg="#444654")
    popup_window67.title("Calculator")
    popup_window67.geometry("605x620")
    popup_window67.resizable(height=False, width=False)
    # Create an Induced Emf layout
    # Create a label Induced Emf
    label1 = tk.Label(popup_window67, text="Induced Emf", font=("Calbiri", 17, "bold"), padx=220, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Magnetic flux and Time.
    magnetic_flux_label = tk.Label(popup_window67, text="Magnetic flux (Wb): ",
                                   font=("Terakatal", 14), bg="#444654")
    magnetic_flux_label.grid(row=1, column=0)
    magnetic_flux_entry = tk.Entry(popup_window67, width=15, font="sans-serif")
    magnetic_flux_entry.grid(row=1, column=1, padx=5, pady=5)

    time_label = tk.Label(popup_window67, text="Time (s): ",
                          font=("Terakatal", 14), bg="#444654")
    time_label.grid(row=2, column=0)
    time_entry = tk.Entry(popup_window67, width=15, font="sans-serif")
    time_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window67, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_induced_emf(magnetic_flux_entry,
                                                                       time_entry,
                                                                       induced_emf_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window67, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear67(magnetic_flux_entry, time_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Induced Emf result.
    induced_emf_label = tk.Label(popup_window67, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    induced_emf_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window67, width=605, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window67, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window67, height=3, width=60, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """INDUCED EMF:       
             Induced Emf can be defined as the generation of a potential 
difference in a coil due to the changes in the magnetic flux through it."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window67, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window67, height=7, width=60, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Induced Emf is:
       ε = - dΦ/dt

    where:
       ε = Induced Emf
      dΦ = Magnetic flux
      dt = Time"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window67.mainloop()


# Create Popup window for Gauss's Law
def popup68():
    popup_window68 = tk.Toplevel(root, bg="#444654")
    popup_window68.title("Calculator")
    popup_window68.geometry("625x580")
    # Create a Gauss's Law layout
    # Create a label Gauss's Law
    label1 = tk.Label(popup_window68, text="Induced Emf", font=("Calbiri", 17, "bold"), padx=230, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Total charge.
    total_charge_label = tk.Label(popup_window68, text="Total charge (C): ",
                                  font=("Terakatal", 14), bg="#444654")
    total_charge_label.grid(row=1, column=0)
    total_charge_entry = tk.Entry(popup_window68, width=15, font="sans-serif")
    total_charge_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window68, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_electric_flux1(total_charge_entry,
                                                                          electric_flux1_label))
    calculate_button.grid(row=2, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window68, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear68(total_charge_entry))
    clear_button.grid(row=2, column=0, padx=5, pady=5)

    # Create a label to display the Electric flux result.
    electric_flux1_label = tk.Label(popup_window68, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    electric_flux1_label.grid(row=3, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window68, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=4, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window68, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=5, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window68, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """GAUSS's LAW:       
        According to Gauss law, the total flux linked with a closed surface is 1/ε0 times the charge enclosed by the closed surface."""
    T.grid(row=6, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window68, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window68, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Gauss's Law is:
      ΦE = Q / ε0

    where:
      ΦE = Electric flux
       Q = Total charge
      ε0 = Electric Constant"""
    T2.grid(row=8, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window68.mainloop()


# Create Popup window for Faraday's Law
def popup69():
    popup_window69 = tk.Toplevel(root, bg="#444654")
    popup_window69.title("Calculator")
    popup_window69.geometry("625x610")
    popup_window69.resizable(height=False, width=False)
    # Create Faraday's Law layout
    # Create a label Faraday's Law
    label1 = tk.Label(popup_window69, text="Faraday's Law", font=("Calbiri", 17, "bold"), padx=220, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Magnetic flux and Time.
    magnetic_flux_label = tk.Label(popup_window69, text="Magnetic flux (Wb): ",
                                   font=("Terakatal", 14), bg="#444654")
    magnetic_flux_label.grid(row=1, column=0)
    magnetic_flux_entry = tk.Entry(popup_window69, width=15, font="sans-serif")
    magnetic_flux_entry.grid(row=1, column=1, padx=5, pady=5)

    time_label = tk.Label(popup_window69, text="Time (s): ",
                          font=("Terakatal", 14), bg="#444654")
    time_label.grid(row=2, column=0)
    time_entry = tk.Entry(popup_window69, width=15, font="sans-serif")
    time_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window69, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_induced_emf1(magnetic_flux_entry,
                                                                        time_entry,
                                                                        induced_emf1_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window69, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear69(magnetic_flux_entry, time_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Induced Emf result.
    induced_emf1_label = tk.Label(popup_window69, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    induced_emf1_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window69, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window69, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window69, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """FARADAY's LAW:
             Faraday law basically states, when the magnetic flux or the 
magnetic field changes with time, the electromotive force is produced."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window69, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window69, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Faraday's Law is:
       ϵ = - dΦ / dt

    where:
       ϵ = Induced Emf
      dΦ = Magnetic flux
      dt = Time"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window69.mainloop()


# Popup window for Modern Physics page formula
# Create Popup window for Time Dilation
def popup70():
    popup_window70 = tk.Toplevel(root, bg="#444654")
    popup_window70.title("Calculator")
    popup_window70.geometry("625x700")
    popup_window70.resizable(height=False, width=False)
    # Create Time Dilation layout
    # Create a label Time Dilation
    label1 = tk.Label(popup_window70, text="Time Dilation", font=("Calbiri", 17, "bold"), padx=220, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Time between 2 colocal events and Velocity.
    time_between_2_colocal_events_label = tk.Label(popup_window70, text="Time between 2 colocal events (s): ",
                                                   font=("Terakatal", 14), bg="#444654")
    time_between_2_colocal_events_label.grid(row=1, column=0)
    time_between_2_colocal_events_entry = tk.Entry(popup_window70, width=15, font="sans-serif")
    time_between_2_colocal_events_entry.grid(row=1, column=1, padx=5, pady=5)

    velocity_label = tk.Label(popup_window70, text="Velocity (s): ",
                              font=("Terakatal", 14), bg="#444654")
    velocity_label.grid(row=2, column=0)
    velocity_entry = tk.Entry(popup_window70, width=15, font="sans-serif")
    velocity_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window70, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_time_between_same_events(time_between_2_colocal_events_entry,
                                                                                    velocity_entry,
                                                                                    time_between_same_events_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window70, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear70(time_between_2_colocal_events_entry, velocity_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Time between same events result.
    time_between_same_events_label = tk.Label(popup_window70, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    time_between_same_events_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window70, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=6, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window70, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=7, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window70, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """TIME DILATION:
             Time dilation is the lengthening of the time interval between two events for an observer in an inertial frame that is moving with respect to the rest frame of the events (in which the events occur at the same 
location)."""
    T.grid(row=8, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window70, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=9, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window70, height=8, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Time Dilation is:
      t' = t / √(1 - v² / c²)

    where:
      t' = Time between same events 
       t = Time between two colocal events
       v = Velocity
       c = Speed of light"""
    T2.grid(row=10, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window70.mainloop()


# Create Popup window for Length Contraction
def popup71():
    popup_window71 = tk.Toplevel(root, bg="#444654")
    popup_window71.title("Calculator")
    popup_window71.geometry("645x640")
    popup_window71.resizable(height=False, width=False)
    # Create Length Contraction layout
    # Create a label Length Contraction
    label1 = tk.Label(popup_window71, text="Length Contraction", font=("Calbiri", 17, "bold"), padx=200, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Proper length and Relative velocity.
    proper_length_label = tk.Label(popup_window71, text="Proper length (m): ",
                                   font=("Terakatal", 14), bg="#444654")
    proper_length_label.grid(row=1, column=0)
    proper_length_entry = tk.Entry(popup_window71, width=15, font="sans-serif")
    proper_length_entry.grid(row=1, column=1, padx=5, pady=5)

    relative_velocity_label = tk.Label(popup_window71, text="Relative velocity (m/s): ",
                                       font=("Terakatal", 14), bg="#444654")
    relative_velocity_label.grid(row=2, column=0)
    relative_velocity_entry = tk.Entry(popup_window71, width=15, font="sans-serif")
    relative_velocity_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window71, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_length_observed(proper_length_entry,
                                                                           relative_velocity_entry,
                                                                           length_observed_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window71, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear71(proper_length_entry, relative_velocity_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Length observed result.
    length_observed_label = tk.Label(popup_window71, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    length_observed_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window71, width=645, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window71, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window71, height=3, width=64, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """LENGTH CONTRACTION:
             A phenomenon in which the length of a moving object is measured to be shorter than its proper length is known as length contraction."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window71, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window71, height=8, width=64, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Length Contraction is:
       L = Lo / √(1 - v² / c²)

    where:
       L = Length observed 
      Lo = Proper length
       v = Relative velocity
       c = Speed of light"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window71.mainloop()


# Create Popup window for Relativistic Mass
def popup72():
    popup_window72 = tk.Toplevel(root, bg="#444654")
    popup_window72.title("Calculator")
    popup_window72.geometry("625x650")
    popup_window72.resizable(height=False, width=False)
    # Create Relativistic Mass layout
    # Create a label Relativistic Mass
    label1 = tk.Label(popup_window72, text="Relativistic Mass", font=("Calbiri", 17, "bold"), padx=200, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Rest mass and Velocity.
    rest_mass_label = tk.Label(popup_window72, text="Rest mass (kg): ",
                               font=("Terakatal", 14), bg="#444654")
    rest_mass_label.grid(row=1, column=0)
    rest_mass_entry = tk.Entry(popup_window72, width=15, font="sans-serif")
    rest_mass_entry.grid(row=1, column=1, padx=5, pady=5)

    velocity_label = tk.Label(popup_window72, text="Velocity (m/s): ",
                              font=("Terakatal", 14), bg="#444654")
    velocity_label.grid(row=2, column=0)
    velocity_entry = tk.Entry(popup_window72, width=15, font="sans-serif")
    velocity_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window72, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_relativistic_mass(rest_mass_entry,
                                                                             velocity_entry,
                                                                             relativistic_mass_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window72, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear72(rest_mass_entry, velocity_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Relativistic Mass result.
    relativistic_mass_label = tk.Label(popup_window72, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    relativistic_mass_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window72, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window72, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window72, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """RELATIVISTIC MASS:
             Relativistic mass is the change in mass of a body which is caused due to the change in the speed of the body."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window72, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window72, height=8, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Relativistic Mass is:
       m = mo / √(1 - v² / c²)

    where:
       m = Relativistic Mass 
      mo = Rest mass
       v = Velocity
       c = Speed of light"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window72.mainloop()


# Create Popup window for Relative Velocity
def popup73():
    popup_window73 = tk.Toplevel(root, bg="#444654")
    popup_window73.title("Calculator")
    popup_window73.geometry("625x650")
    popup_window73.resizable(height=False, width=False)
    # Create Relative Velocity layout
    # Create a label Relative Velocity
    label1 = tk.Label(popup_window73, text="Relative Velocity", font=("Calbiri", 17, "bold"), padx=200, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Velocity of A and Velocity of B.
    velocity_of_a_label = tk.Label(popup_window73, text="Velocity of A (m/s): ",
                                   font=("Terakatal", 14), bg="#444654")
    velocity_of_a_label.grid(row=1, column=0)
    velocity_of_a_entry = tk.Entry(popup_window73, width=15, font="sans-serif")
    velocity_of_a_entry.grid(row=1, column=1, padx=5, pady=5)

    velocity_of_b_label = tk.Label(popup_window73, text="Velocity of B (m/s): ",
                                   font=("Terakatal", 14), bg="#444654")
    velocity_of_b_label.grid(row=2, column=0)
    velocity_of_b_entry = tk.Entry(popup_window73, width=15, font="sans-serif")
    velocity_of_b_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window73, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_relative_velocity(velocity_of_a_entry,
                                                                             velocity_of_b_entry,
                                                                             relative_velocity_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window73, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear73(velocity_of_a_entry, velocity_of_b_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Relative Velocity result.
    relative_velocity_label = tk.Label(popup_window73, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    relative_velocity_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window73, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window73, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window73, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """RELATIVE VELOCITY:
               Relative velocity is defined as the velocity of an object B in the 
rest frame of another object A."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window73, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window73, height=8, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Relative Velocity is:
      u' = (u + v) / (1 + uv / c²)

    where:
      u' = Relative Velocity 
       u = Velocity of A
       v = Velocity of B
       c = Speed of light"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window73.mainloop()


# Create Popup window for Relativistic Momentum
def popup74():
    popup_window74 = tk.Toplevel(root, bg="#444654")
    popup_window74.title("Calculator")
    popup_window74.geometry("635x680")
    popup_window74.resizable(height=False, width=False)
    # Create Relativistic Momentum layout
    # Create a label Relativistic Momentum
    label1 = tk.Label(popup_window74, text="Relativistic Momentum", font=("Calbiri", 17, "bold"), padx=170, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Mass and Velocity.
    mass_label = tk.Label(popup_window74, text="Mass (kg): ",
                          font=("Terakatal", 14), bg="#444654")
    mass_label.grid(row=1, column=0)
    mass_entry = tk.Entry(popup_window74, width=15, font="sans-serif")
    mass_entry.grid(row=1, column=1, padx=5, pady=5)

    velocity_label = tk.Label(popup_window74, text="Velocity (m/s): ",
                              font=("Terakatal", 14), bg="#444654")
    velocity_label.grid(row=2, column=0)
    velocity_entry = tk.Entry(popup_window74, width=15, font="sans-serif")
    velocity_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window74, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_relativistic_momentum(mass_entry,
                                                                                 velocity_entry,
                                                                                 relativistic_momentum_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window74, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear74(mass_entry, velocity_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Relativistic Momentum result.
    relativistic_momentum_label = tk.Label(popup_window74, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    relativistic_momentum_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window74, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window74, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window74, height=5, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """RELATIVISTIC MOMENTUM:
             Relativistic momentum is the momentum of an object when taking into account the effects of special relativity, which include time dilation and length contraction. In other words, it is the momentum of an object 
traveling at a significant fraction of the speed of light."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window74, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window74, height=8, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Relativistic Momentum is:
       p = (m . v) / √(1 - v² / c²)

    where:
       p = Momentum
       m = Mass
       v = Velocity 
       c = Speed of light"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window74.mainloop()


# Create Popup window for Energy-Momentum
def popup75():
    popup_window75 = tk.Toplevel(root, bg="#444654")
    popup_window75.title("Calculator")
    popup_window75.geometry("625x660")
    popup_window75.resizable(height=False, width=False)
    # Create Energy-Momentum layout
    # Create a label Energy-Momentum
    label1 = tk.Label(popup_window75, text="Energy-Momentum", font=("Calbiri", 17, "bold"), padx=190, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Momentum and Rest mass.
    momentum_label = tk.Label(popup_window75, text="Momentum (kgm/s): ",
                              font=("Terakatal", 14), bg="#444654")
    momentum_label.grid(row=1, column=0)
    momentum_entry = tk.Entry(popup_window75, width=15, font="sans-serif")
    momentum_entry.grid(row=1, column=1, padx=5, pady=5)

    rest_mass_label = tk.Label(popup_window75, text="Rest mass (kg): ",
                               font=("Terakatal", 14), bg="#444654")
    rest_mass_label.grid(row=2, column=0)
    rest_mass_entry = tk.Entry(popup_window75, width=15, font="sans-serif")
    rest_mass_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window75, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_energy_momentum(momentum_entry,
                                                                           rest_mass_entry,
                                                                           energy_momentum_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window75, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear75(momentum_entry, rest_mass_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Energy-Momentum result.
    energy_momentum_label = tk.Label(popup_window75, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    energy_momentum_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window75, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window75, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window75, height=4, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """ENERGY-MOMENTUM:
             The energy-momentum relation is a relativistic equation that can be used to link an object’s mass, total energy, and momentum while it is at rest."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window75, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window75, height=8, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Energy-Momentum is:
      E² = p².c² + (mo.c²)²

    where:
      E = Energy
      p = Momentum
     mo = Rest Mass
      c = Speed of light"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window75.mainloop()


# Create Popup window for Mass-Energy
def popup76():
    popup_window76 = tk.Toplevel(root, bg="#444654")
    popup_window76.title("Calculator")
    popup_window76.geometry("635x630")
    popup_window76.resizable(height=False, width=False)
    # Create Mass-Energy layout
    # Create a label Mass-Energy
    label1 = tk.Label(popup_window76, text="Mass-Energy", font=("Calbiri", 17, "bold"), padx=230, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Mass.
    mass_label = tk.Label(popup_window76, text="Mass (kg): ",
                          font=("Terakatal", 14), bg="#444654")
    mass_label.grid(row=1, column=0)
    mass_entry = tk.Entry(popup_window76, width=15, font="sans-serif")
    mass_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window76, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_mass_energy(mass_entry, mass_energy_label))
    calculate_button.grid(row=2, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window76, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear76(mass_entry))
    clear_button.grid(row=2, column=0, padx=5, pady=5)

    # Create a label to display the Mass-Energy result.
    mass_energy_label = tk.Label(popup_window76, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    mass_energy_label.grid(row=3, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window76, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window76, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window76, height=5, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """MASS-ENERGY:
             The "mass-energy equivalence" principle states that the mass of a system and its energy are the same property in any physical system. This means that anything having mass has an equivalent amount of energy 
and vice versa."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window76, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window76, height=7, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Mass-Energy is:
       E = m.c²

    where:
      E = Energy
      m = Mass
      c = Speed of light"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window76.mainloop()


# Create Popup window for Relativistic Doppler Effect
def popup77():
    popup_window77 = tk.Toplevel(root, bg="#444654")
    popup_window77.title("Calculator")
    popup_window77.geometry("625x650")
    popup_window77.resizable(height=False, width=False)
    # Create Relativistic Doppler Effect layout
    # Create a label Relativistic Doppler Effect
    label1 = tk.Label(popup_window77, text="Relativistic Doppler Effect", font=("Calbiri", 17, "bold"), padx=150, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Wavelength and Velocity.
    wavelength_label = tk.Label(popup_window77, text="Wavelength (m): ",
                                font=("Terakatal", 14), bg="#444654")
    wavelength_label.grid(row=1, column=0)
    wavelength_entry = tk.Entry(popup_window77, width=15, font="sans-serif")
    wavelength_entry.grid(row=1, column=1, padx=5, pady=5)

    velocity_label = tk.Label(popup_window77, text="Velocity (m/s): ", font=("Terakatal", 14), bg="#444654")
    velocity_label.grid(row=2, column=0)
    velocity_entry = tk.Entry(popup_window77, width=15, font="sans-serif")
    velocity_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window77, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_perceived_wavelength(wavelength_entry,
                                                                                velocity_entry,
                                                                                perceived_wavelength_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window77, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear77(wavelength_entry, velocity_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a label to display the Perceived Wavelength result.
    perceived_wavelength_label = tk.Label(popup_window77, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    perceived_wavelength_label.grid(row=4, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window77, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window77, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window77, height=3, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """RELATIVISTIC DOPPLER EFFECT:
                 The relativistic Doppler Effect is some alteration in frequency 
caused when there is relativistic motion between observer and source."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window77, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window77, height=8, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Relativistic Doppler Effect is:
    λ' / λ =  √(1 + v/c) / √(1 - v/c)

    where:
        λ' = Perceived wavelength
         λ = Wavelength
         v = Velocity
         c = Speed of light"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window77.mainloop()


# Create Popup window for Photon Energy
def popup78():
    popup_window78 = tk.Toplevel(root, bg="#444654")
    popup_window78.title("Calculator")
    popup_window78.geometry("625x640")
    popup_window78.resizable(height=False, width=False)
    # Create Photon Energy layout
    # Create a label Photon Energy
    label1 = tk.Label(popup_window78, text="Photon Energy", font=("Calbiri", 17, "bold"), padx=150, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Frequency.
    frequency_label = tk.Label(popup_window78, text="Frequency (1/s): ",
                               font=("Terakatal", 14), bg="#444654")
    frequency_label.grid(row=1, column=0)
    frequency_entry = tk.Entry(popup_window78, width=15, font="sans-serif")
    frequency_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window78, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_photon_energy(frequency_entry, photon_energy_label))
    calculate_button.grid(row=2, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window78, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear78(frequency_entry))
    clear_button.grid(row=2, column=0, padx=5, pady=5)

    # Create a label to display the Photon Energy result.
    photon_energy_label = tk.Label(popup_window78, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    photon_energy_label.grid(row=3, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window78, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window78, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window78, height=5, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """PHOTON ENERGY:
                 The "mass-energy equivalence" principle states that the mass 
of a system and its energy are the same property in any physical system. This means that anything having mass has an equivalent amount of 
energy and vice versa."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window78, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window78, height=7, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Photon Energy is:
       p = h / λ

    where:
       p = Momentum of the photon
       λ = Wavelength
       h = Planck Constant"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window78.mainloop()


# Create Popup window for Half-Life
def popup79():
    popup_window79 = tk.Toplevel(root, bg="#444654")
    popup_window79.title("Calculator")
    popup_window79.geometry("625x570")
    popup_window79.resizable(height=False, width=False)
    # Create Half-Life layout
    # Create a label Half-Life
    label1 = tk.Label(popup_window79, text="Half Life", font=("Calbiri", 17, "bold"), padx=250, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for Decay constant.
    decay_constant_label = tk.Label(popup_window79, text="Decay constant : ",
                                    font=("Terakatal", 14), bg="#444654")
    decay_constant_label.grid(row=1, column=0)
    decay_constant_entry = tk.Entry(popup_window79, width=15, font="sans-serif")
    decay_constant_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window79, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_half_life(decay_constant_entry, half_life_label))
    calculate_button.grid(row=2, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window79, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear79(decay_constant_entry))
    clear_button.grid(row=2, column=0, padx=5, pady=5)

    # Create a label to display the Decay constant result.
    half_life_label = tk.Label(popup_window79, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    half_life_label.grid(row=3, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window79, width=625, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window79, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window79, height=4, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """HALF-LIFE:
             Half-Life is defined as the time needed by a radioactive substance (or one half the atoms) to disintegrate or transform into a different 
substance. """
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window79, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window79, height=6, width=62, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Half Life is:
     t½ = ln(2) / λ

    where:
        t = Half Life
        λ = Decay constant"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window79.mainloop()


# Create Popup window for Photon Momentum
def popup80():
    popup_window80 = tk.Toplevel(root, bg="#444654")
    popup_window80.title("Calculator")
    popup_window80.geometry("635x630")
    popup_window80.resizable(height=False, width=False)
    # Create Photon Momentum layout
    # Create a label Photon Momentum
    label1 = tk.Label(popup_window80, text="Photon Momentum", font=("Calbiri", 17, "bold"), padx=190, pady=5,
                      fg="#3A98B9", bd=1, borderwidth=2, relief="solid", bg="#18122b")
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Create labels and entries for wavelength.
    wavelength_label = tk.Label(popup_window80, text="Wavelength (m): ",
                                font=("Terakatal", 14), bg="#444654")
    wavelength_label.grid(row=1, column=0)
    wavelength_entry = tk.Entry(popup_window80, width=15, font="sans-serif")
    wavelength_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a calculate and clear button.
    calculate_button = tk.Button(popup_window80, text="Calculate", borderwidth=2, font=("Terakatal", 12),
                                 command=lambda: calculate_momentum_of_the_photon(wavelength_entry,
                                                                                  momentum_of_the_photon_label))
    calculate_button.grid(row=2, column=1, padx=5, pady=5)

    clear_button = tk.Button(popup_window80, text="Clear", borderwidth=2, font=("Terakatal", 12),
                             command=lambda: clear80(wavelength_entry))
    clear_button.grid(row=2, column=0, padx=5, pady=5)

    # Create a label to display the Maximum Kinetic Energy result.
    momentum_of_the_photon_label = tk.Label(popup_window80, fg="#0002a1", font=("Verdana", 14), bg="#444654")
    momentum_of_the_photon_label.grid(row=3, column=1, padx=10, pady=10)

    # Create a Horizontal line in the main frame
    canvas1 = tk.Canvas(popup_window80, width=635, height=2, background="black", bd=-1)
    canvas1.grid(row=5, column=0, columnspan=2)

    # Definition
    lab = tk.Label(popup_window80, text="Definition", font=("Calbiri", 16, "bold underline"), bg="#444654")
    lab.grid(row=6, columnspan=2, padx=5, pady=5)

    T = tk.Text(popup_window80, height=5, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    Def = """PHOTON MOMENTUM:
             Photon momentum refers to the momentum of a photon, which is a massless particle of light. In classical physics, momentum is defined as 
mass times velocity, but since photons have zero rest mass, their 
momentum is defined in terms of their frequency and wavelength."""
    T.grid(row=7, column=0, columnspan=4, sticky="w")

    # Insert the Definition
    T.insert(tk.END, Def)

    # Formula
    lab = tk.Label(popup_window80, text="Formula", font=("Calbiri", 16, "bold underline"), bg="#444654", underline=6)
    lab.grid(row=8, columnspan=2, padx=5, pady=5)

    T2 = tk.Text(popup_window80, height=7, width=63, font=("Terakatal", 13), bg="grey", borderwidth=1)
    For1 = """The formula for Photon Momentum is:
       p = h / λ

    where:
       p = Momentum of the photon 
       λ = Wavelength
       h = Planck constant"""
    T2.grid(row=9, column=0, columnspan=7, sticky="w")

    # Insert the Formula
    T2.insert(tk.END, For1)
    popup_window80.mainloop()


# Mechanics
# Velocity page
def velocity_page():
    velocity_frame = tk.Frame(main_frame1)
    velocity_frame.pack()
    popup()


# Acceleration page
def acceleration_page():
    acceleration_frame = tk.Frame(main_frame)
    acceleration_frame.pack()
    popup1()


# Equation of motion page
def equation_of_motion_page():
    equation_of_motion_frame = tk.Frame(main_frame)
    equation_of_motion_frame.pack()
    popup2()


# Force page
def force_page():
    force_frame = tk.Frame(main_frame)
    force_frame.pack()
    popup3()


# Centripetal acceleration page
def centripetal_acceleration_page():
    centripetal_acceleration_frame = tk.Frame(main_frame)
    centripetal_acceleration_frame.pack()
    popup4()


# Momentum page
def momentum_page():
    momentum_frame = tk.Frame(main_frame)
    momentum_frame.pack()
    popup5()


# Impulse page
def impulse_page():
    impulse_frame = tk.Frame(main_frame)
    impulse_frame.pack()
    popup6()


# Work page
def work_page():
    work_frame = tk.Frame(main_frame)
    work_frame.pack()
    popup7()


# Kinetic energy page
def kinetic_energy_page():
    kinetic_frame = tk.Frame(main_frame)
    kinetic_frame.pack()
    popup8()


# Potential energy page
def potential_energy_page():
    potential_frame = tk.Frame(main_frame)
    potential_frame.pack()
    popup9()


# Efficiency energy page
def efficiency_page():
    efficiency_frame = tk.Frame(main_frame)
    efficiency_frame.pack()
    popup10()


# Power page
def power_page():
    power_frame = tk.Frame(main_frame)
    power_frame.pack()
    popup11()


# Angular Velocity page
def angular_velocity_page():
    angular_velocity_frame = tk.Frame(main_frame)
    angular_velocity_frame.pack()
    popup12()


# Angular Acceleration page
def angular_acceleration_page():
    angular_acceleration_frame = tk.Frame(main_frame)
    angular_acceleration_frame.pack()
    popup13()


# Torque page
def torque_page():
    torque_frame = tk.Frame(main_frame)
    torque_frame.pack()
    popup14()


# Moment of Inertia page
def moment_of_inertia_page():
    moment_of_inertia_frame = tk.Frame(main_frame)
    moment_of_inertia_frame.pack()
    popup15()


# Angular Momentum page
def angular_momentum_page():
    angular_momentum_frame = tk.Frame(main_frame)
    angular_momentum_frame.pack()
    popup16()


# Universal Gravitation page
def universal_gravitation_page():
    universal_gravitation_frame = tk.Frame(main_frame)
    universal_gravitation_frame.pack()
    popup17()


# Simple Pendulum page
def simple_pendulum_page():
    simple_pendulum_frame = tk.Frame(main_frame)
    simple_pendulum_frame.pack()
    popup18()


# Frequency page
def frequency_page():
    frequency_frame = tk.Frame(main_frame)
    frequency_frame.pack()
    popup19()


# Density page
def density_page():
    density_frame = tk.Frame(main_frame)
    density_frame.pack()
    popup20()


# Pressure page
def pressure_page():
    pressure_frame = tk.Frame(main_frame)
    pressure_frame.pack()
    popup21()


# Kinematic Viscosity page
def kinematic_viscosity_page():
    kinetic_viscosity_frame = tk.Frame(main_frame)
    kinetic_viscosity_frame.pack()
    popup22()


# Surface Tension page
def surface_tension_page():
    surface_tension_frame = tk.Frame(main_frame)
    surface_tension_frame.pack()
    popup23()


# Thermal Physics
# Sensible Heat page
def sensible_heat_page():
    sensible_heat_frame = tk.Frame(main_frame)
    sensible_heat_frame.pack()
    popup24()


# Latent Heat page
def latent_heat_page():
    latent_heat_frame = tk.Frame(main_frame)
    latent_heat_frame.pack()
    popup25()


# Ideal Gas Law page
def ideal_gas_law_page():
    ideal_gas_law_frame = tk.Frame(main_frame)
    ideal_gas_law_frame.pack()
    popup26()


# Stefan-Boltzmann Law page
def stefan_boltzmann_law_page():
    stefan_boltzmann_law_frame = tk.Frame(main_frame)
    stefan_boltzmann_law_frame.pack()
    popup27()


# Thermal Energy page
def thermal_energy_page():
    thermal_energy_frame = tk.Frame(main_frame)
    thermal_energy_frame.pack()
    popup28()


# Gibbs free energy page
def gibbs_free_energy_page():
    gibbs_free_energy_frame = tk.Frame(main_frame)
    gibbs_free_energy_frame.pack()
    popup29()


# Thermodynamic Work page
def thermodynamic_work_page():
    thermodynamic_work_frame = tk.Frame(main_frame)
    thermodynamic_work_frame.pack()
    popup30()


# 1st Law of Thermodynamic page
def first_law_of_thermodynamic_page():
    first_law_of_thermodynamic_frame = tk.Frame(main_frame)
    first_law_of_thermodynamic_frame.pack()
    popup31()


# Entropy page
def entropy_page():
    entropy_frame = tk.Frame(main_frame)
    entropy_frame.pack()
    popup32()


# Thermal efficiency page
def thermal_efficiency_page():
    thermal_efficiency_frame = tk.Frame(main_frame)
    thermal_efficiency_frame.pack()
    popup33()


# C.O.P page
def c_o_p_page():
    c_o_p_frame = tk.Frame(main_frame)
    c_o_p_frame.pack()
    popup34()


# Waves and Optics
# Periodic Waves page
def periodic_waves_page():
    periodic_waves_frame = tk.Frame(main_frame)
    periodic_waves_frame.pack()
    popup35()


# Beat frequency page
def beat_frequency_page():
    beat_frequency_frame = tk.Frame(main_frame)
    beat_frequency_frame.pack()
    popup36()


# Intensity page
def intensity_page():
    intensity_frame = tk.Frame(main_frame)
    intensity_frame.pack()
    popup37()


# Intensity Level page
def sound_intensity_level_page():
    sound_intensity_level_frame = tk.Frame(main_frame)
    sound_intensity_level_frame.pack()
    popup38()


# Pressure Level page
def sound_pressure_level_page():
    sound_pressure_level_frame = tk.Frame(main_frame)
    sound_pressure_level_frame.pack()
    popup39()


# Index of Refraction page
def refractive_index_page():
    refractive_index_frame = tk.Frame(main_frame)
    refractive_index_frame.pack()
    popup40()


# Snell's Law page
def snell_law_page():
    snell_law_frame = tk.Frame(main_frame)
    snell_law_frame.pack()
    popup41()


# Critical Angle page
def critical_angle_page():
    critical_angle_frame = tk.Frame(main_frame)
    critical_angle_frame.pack()
    popup42()


# Focal Length page
def focal_length_page():
    focal_length_frame = tk.Frame(main_frame)
    focal_length_frame.pack()
    popup43()


# Magnification page
def magnification_page():
    magnification_frame = tk.Frame(main_frame)
    magnification_frame.pack()
    popup44()


# Spherical Mirrors page
def spherical_mirrors_page():
    spherical_mirrors_frame = tk.Frame(main_frame)
    spherical_mirrors_frame.pack()
    popup45()


# Electricity and Magnetism
# Coulomb's Law page
def coulomb_law_page():
    coulomb_law_frame = tk.Frame(main_frame)
    coulomb_law_frame.pack()
    popup46()


# Electric field page
def electric_field_page():
    electric_field_frame = tk.Frame(main_frame)
    electric_field_frame.pack()
    popup47()


# Electric potential page
def electric_potential_page():
    electric_potential_frame = tk.Frame(main_frame)
    electric_potential_frame.pack()
    popup48()


# Capacitance page
def capacitance_page():
    capacitance_frame = tk.Frame(main_frame)
    capacitance_frame.pack()
    popup49()


# Parallel Plate Capacitor page
def parallel_plate_capacitor_page():
    parallel_plate_capacitor_frame = tk.Frame(main_frame)
    parallel_plate_capacitor_frame.pack()
    popup50()


# Electric current page
def electric_current_page():
    electric_current_frame = tk.Frame(main_frame)
    electric_current_frame.pack()
    popup51()


# Ohm's Law page
def ohm_law_page():
    ohm_law_frame = tk.Frame(main_frame)
    ohm_law_frame.pack()
    popup52()


# Electric Resistance page
def electrical_resistance_page():
    electrical_resistance_frame = tk.Frame(main_frame)
    electrical_resistance_frame.pack()
    popup53()


# Resistors in Series page
def resistors_in_series_page():
    resistors_in_series_frame = tk.Frame(main_frame)
    resistors_in_series_frame.pack()
    popup54()


# Resistors in Parallel page
def resistors_in_parallel_page():
    resistors_in_parallel_frame = tk.Frame(main_frame)
    resistors_in_parallel_frame.pack()
    popup55()


# Capacitors in Series page
def capacitors_in_series_page():
    capacitors_in_series_frame = tk.Frame(main_frame)
    capacitors_in_series_frame.pack()
    popup56()


# Capacitors in Parallel page
def capacitors_in_parallel_page():
    capacitors_in_parallel_frame = tk.Frame(main_frame)
    capacitors_in_parallel_frame.pack()
    popup57()


# Magnetic Force(Charge) page
def magnetic_force_page():
    magnetic_force_frame = tk.Frame(main_frame)
    magnetic_force_frame.pack()
    popup58()


# Magnetic Force(Current) page
def magnetic_force1_page():
    magnetic_force1_frame = tk.Frame(main_frame)
    magnetic_force1_frame.pack()
    popup59()


# Magnetic Field page
def magnetic_field_page():
    magnetic_field_frame = tk.Frame(main_frame)
    magnetic_field_frame.pack()
    popup60()


# Solenoid(Magnetic Field) page
def solenoid_page():
    solenoid_frame = tk.Frame(main_frame)
    solenoid_frame.pack()
    popup61()


# Straight Wire(Magnetic Field) page
def straight_wire_page():
    straight_wire_frame = tk.Frame(main_frame)
    straight_wire_frame.pack()
    popup62()


# Parallel Wire(Magnetic force) page
def parallel_wire_page():
    parallel_wire_frame = tk.Frame(main_frame)
    parallel_wire_frame.pack()
    popup63()


# Electric flux page
def electric_flux_page():
    electric_flux_frame = tk.Frame(main_frame)
    electric_flux_frame.pack()
    popup64()


# Magnetic flux page
def magnetic_flux_page():
    magnetic_flux_frame = tk.Frame(main_frame)
    magnetic_flux_frame.pack()
    popup65()


# Motional Emf page
def motional_emf_page():
    motional_emf_frame = tk.Frame(main_frame)
    motional_emf_frame.pack()
    popup66()


# Induced Emf page
def induced_emf_page():
    induced_emf_frame = tk.Frame(main_frame)
    induced_emf_frame.pack()
    popup67()


# Gauss's Law page
def gauss_law_page():
    gauss_law_frame = tk.Frame(main_frame)
    gauss_law_frame.pack()
    popup68()


# Faraday's Law page
def faraday_law_page():
    faraday_law_frame = tk.Frame(main_frame)
    faraday_law_frame.pack()
    popup69()


# Modern Physics
# Time Dilation page
def time_dilation_page():
    time_dilation_frame = tk.Frame(main_frame)
    time_dilation_frame.pack()
    popup70()


# Length Contraction page
def length_contraction_page():
    length_contraction_frame = tk.Frame(main_frame)
    length_contraction_frame.pack()
    popup71()


# Relativistic Mass page
def relativistic_mass_page():
    relativistic_mass_frame = tk.Frame(main_frame)
    relativistic_mass_frame.pack()
    popup72()


# Relative Velocity page
def relative_velocity_page():
    relative_velocity_frame = tk.Frame(main_frame)
    relative_velocity_frame.pack()
    popup73()


# Relativistic Momentum page
def relativistic_momentum_page():
    relativistic_momentum_frame = tk.Frame(main_frame)
    relativistic_momentum_frame.pack()
    popup74()


# Energy-Momentum page
def energy_momentum_page():
    energy_momentum_frame = tk.Frame(main_frame)
    energy_momentum_frame.pack()
    popup75()


# Mass-Energy page
def mass_energy_page():
    mass_energy_frame = tk.Frame(main_frame)
    mass_energy_frame.pack()
    popup76()


# Relativistic Doppler Effect page
def relativistic_doppler_effect_page():
    relativistic_doppler_effect_frame = tk.Frame(main_frame)
    relativistic_doppler_effect_frame.pack()
    popup77()


# Photon Energy page
def photon_energy_page():
    photon_energy_frame = tk.Frame(main_frame)
    photon_energy_frame.pack()
    popup78()


# Half-Life page
def half_life_page():
    half_life_frame = tk.Frame(main_frame)
    half_life_frame.pack()
    popup79()


# Photon Momentum page
def photon_momentum_page():
    photon_momentum_frame = tk.Frame(main_frame)
    photon_momentum_frame.pack()
    popup80()


def hide_indicator():
    mechanics_indicator.config(bg="#c3c3c3")
    thermal_physics_indicator.config(bg="#c3c3c3")
    wave_and_optics_indicator.config(bg="#c3c3c3")
    electricity_and_magnetism_indicator.config(bg="#c3c3c3")
    modern_physics_indicator.config(bg="#c3c3c3")


def delete_page():
    for frame in main_frame1.winfo_children():
        frame.destroy()


def indicate(lb, page):
    hide_indicator()
    lb.config(bg="#158aff")
    delete_page()
    page()


# Mechanics page
def mechanics_page():
    mechanics_frame = tk.Frame(main_frame1)
    mechanics_frame.pack()

    # Create a Vertical line in the main frame
    canvas1 = tk.Canvas(main_frame1, width=2, height=800, background="black", bd=-1)
    canvas1.pack()

    label = tk.Label(main_frame1, text="FORMULA", font=font1, bg="#3e497a", padx=25, pady=5, width=43, borderwidth=1,
                     relief="solid")  # 567189    413543
    label.place(x=10, y=5)

    # Velocity button
    velocity_btn = tk.Button(main_frame1, text="Velocity", font=("Verdana", 15), bd=1, fg="#3A98B9", borderwidth=3,
                             highlightbackground="black", width=17,
                             bg="#18122b", command=velocity_page)
    velocity_btn.place(x=25, y=70)
    # velocity_indicator = tk.Label(main_frame1, text="", bg="#c3c3c3")
    # velocity_indicator.place(x=3, y=50, width=5, height=40)

    # Acceleration button
    acceleration_btn = tk.Button(main_frame1, text="Acceleration", font=("Verdana", 15), bd=0, fg="#3A98B9",
                                 borderwidth=3, highlightbackground="black",
                                 bg="#18122b", width=17, command=acceleration_page)  # 158aff
    acceleration_btn.place(x=25, y=120)
    # acceleration_indicator = tk.Label(main_frame, text="", bg="#c3c3c3")  # c3c3c3
    # acceleration_indicator.place(x=3, y=100, width=5, height=40)

    # Equation of motion button
    equation_of_motion_btn = tk.Button(main_frame1, text="Equation of Motion", font=("Verdana", 15), bd=0, fg="#3A98B9",
                                       borderwidth=3, highlightbackground="black",
                                       bg="#18122b", width=17, command=equation_of_motion_page)  # bg="#121212"
    equation_of_motion_btn.place(x=25, y=170)
    # equation_of_motion_indicator = tk.Label(main_frame, text="", bg="#c3c3c3")
    # equation_of_motion_indicator.place(x=3, y=150, width=5, height=40)

    # Force button
    force_btn = tk.Button(main_frame1, text="Force", font=("Verdana", 15), bd=0, fg="#3A98B9", borderwidth=3,
                          highlightbackground="black",
                          bg="#18122b", width=17, command=force_page)
    force_btn.place(x=25, y=220)
    # force_indicator = tk.Label(main_frame, text="", bg="#c3c3c3")
    # force_indicator.place(x=3, y=200, width=5, height=40)

    # Centripetal acceleration button
    centripetal_acceleration_btn = tk.Button(main_frame1, text="Centripetal\nAcceleration",
                                             font=("Verdana", 15), bd=0, width=17, fg="#3A98B9", borderwidth=3,
                                             highlightbackground="black", bg="#18122b",
                                             command=centripetal_acceleration_page)
    centripetal_acceleration_btn.place(x=25, y=270)
    # centripetal_acceleration_indicator = tk.Label(main_frame, text="", bg="#c3c3c3")
    # centripetal_acceleration_indicator.place(x=3, y=250, width=5, height=68)

    # Momentum button
    momentum_btn = tk.Button(main_frame1, text="Momentum", font=("Verdana", 15), bd=0, fg="#3A98B9", borderwidth=3,
                             highlightbackground="black", width=17,
                             bg="#18122b", command=momentum_page)
    momentum_btn.place(x=25, y=350)
    # momentum_indicator = tk.Label(main_frame, text="", bg="#c3c3c3")
    # momentum_indicator.place(x=3, y=330, width=5, height=40)

    # Impulse button
    impulse_btn = tk.Button(main_frame1, text="Impulse", font=("Verdana", 15), bd=0, fg="#3A98B9", borderwidth=3,
                            highlightbackground="black", width=17,
                            bg="#18122b", command=impulse_page)
    impulse_btn.place(x=25, y=400)
    # impulse_indicator = tk.Label(option_frame, text="", bg="#c3c3c3")
    # impulse_indicator.place(x=3, y=380, width=5, height=40)

    # Work button
    work_btn = tk.Button(main_frame1, text="Work", font=("Verdana", 15), bd=0, fg="#3A98B9", borderwidth=3,
                         highlightbackground="black", width=17, bg="#18122b",
                         command=work_page)
    work_btn.place(x=25, y=450)

    # Kinetic energy button
    kinetic_energy_btn = tk.Button(main_frame1, text="Kinetic energy", font=("Verdana", 15), bd=0, fg="#3A98B9",
                                   borderwidth=3, highlightbackground="black",
                                   width=17, bg="#18122b", command=kinetic_energy_page)
    kinetic_energy_btn.place(x=25, y=500)

    # Potential energy button
    potential_energy_btn = tk.Button(main_frame1, text="Potential energy", font=("Verdana", 15), bd=0, fg="#3A98B9",
                                     borderwidth=3, highlightbackground="black",
                                     width=17, bg="#18122b", command=potential_energy_page)
    potential_energy_btn.place(x=25, y=550)

    # Efficiency button
    efficiency_btn = tk.Button(main_frame1, text="Efficiency", font=("Verdana", 15), bd=0, fg="#3A98B9", borderwidth=3,
                               highlightbackground="black",
                               width=17, bg="#18122b", command=efficiency_page)
    efficiency_btn.place(x=25, y=600)

    # Power button
    power_btn = tk.Button(main_frame1, text="Power", font=("Verdana", 15), bd=0, fg="#3A98B9", borderwidth=3,
                          highlightbackground="black",
                          width=17, bg="#18122b", command=power_page)
    power_btn.place(x=25, y=650)

    # Angular Velocity button
    angular_velocity_btn = tk.Button(main_frame1, text="Angular Velocity", font=("Verdana", 15), bd=0, fg="#3A98B9",
                                     borderwidth=3, highlightbackground="black",
                                     width=17, bg="#18122b", command=angular_velocity_page)
    angular_velocity_btn.place(x=25, y=700)

    # Angular Acceleration button
    angular_acceleration_btn = tk.Button(main_frame1, text="Angular Acceleration", font=("Verdana", 15), bd=0,
                                         fg="#3A98B9", borderwidth=3, highlightbackground="black",
                                         width=17, bg="#18122b", command=angular_acceleration_page)
    angular_acceleration_btn.place(x=310, y=70)

    # Torque button
    torque_btn = tk.Button(main_frame1, text="Torque", font=("Verdana", 15), bd=0,
                           fg="#3A98B9", borderwidth=3, highlightbackground="black",
                           width=17, bg="#18122b", command=torque_page)
    torque_btn.place(x=310, y=120)

    # Moment of Inertia button
    moment_of_inertia_btn = tk.Button(main_frame1, text="Moment of Inertia", font=("Verdana", 15), bd=0,
                                      fg="#3A98B9", borderwidth=3, highlightbackground="black",
                                      width=17, bg="#18122b", command=moment_of_inertia_page)
    moment_of_inertia_btn.place(x=310, y=170)

    # Angular Momentum button
    angular_momentum_btn = tk.Button(main_frame1, text="Angular Momentum", font=("Verdana", 15), bd=0,
                                     fg="#3A98B9", borderwidth=3, highlightbackground="black",
                                     width=17, bg="#18122b", command=angular_momentum_page)
    angular_momentum_btn.place(x=310, y=220)

    # Universal Gravitation button
    universal_gravitation_btn = tk.Button(main_frame1, text="Universal Gravitation", font=("Verdana", 15), bd=0,
                                          fg="#3A98B9", borderwidth=3, highlightbackground="black",
                                          width=17, bg="#18122b", command=universal_gravitation_page)
    universal_gravitation_btn.place(x=310, y=270)

    # Simple Pendulum button
    simple_pendulum_btn = tk.Button(main_frame1, text="Simple Pendulum", font=("Verdana", 15), bd=0,
                                    fg="#3A98B9", borderwidth=3, highlightbackground="black",
                                    width=17, bg="#18122b", command=simple_pendulum_page)
    simple_pendulum_btn.place(x=310, y=320)

    # Frequency button
    frequency_btn = tk.Button(main_frame1, text="Frequency", font=("Verdana", 15), bd=0,
                              fg="#3A98B9", borderwidth=3, highlightbackground="black",
                              width=17, bg="#18122b", command=frequency_page)
    frequency_btn.place(x=310, y=370)

    # Density button
    density_btn = tk.Button(main_frame1, text="Density", font=("Verdana", 15), bd=0,
                            fg="#3A98B9", borderwidth=3, highlightbackground="black",
                            width=17, bg="#18122b", command=density_page)
    density_btn.place(x=310, y=420)

    # Pressure button
    pressure_btn = tk.Button(main_frame1, text="Pressure", font=("Verdana", 15), bd=0,
                             fg="#3A98B9", borderwidth=3, highlightbackground="black",
                             width=17, bg="#18122b", command=pressure_page)
    pressure_btn.place(x=310, y=470)

    # Kinetic Viscosity button
    kinematic_viscosity_btn = tk.Button(main_frame1, text="Kinematic Viscosity", font=("Verdana", 15), bd=0,
                                        fg="#3A98B9", borderwidth=3, highlightbackground="black",
                                        width=17, bg="#18122b", command=kinematic_viscosity_page)
    kinematic_viscosity_btn.place(x=310, y=520)

    # Surface Tension button
    surface_tension_btn = tk.Button(main_frame1, text="Surface Tension", font=("Verdana", 15), bd=0,
                                    fg="#3A98B9", borderwidth=3, highlightbackground="black",
                                    width=17, bg="#18122b", command=surface_tension_page)
    surface_tension_btn.place(x=310, y=570)


# Thermal Physics page
def thermal_physics_page():
    thermal_physics_frame = tk.Frame(main_frame)
    thermal_physics_frame.pack()

    # Create a label for Formula
    label = tk.Label(main_frame1, text="FORMULA", font=font1, bg="#3e497a", padx=25, pady=5, width=43, borderwidth=1,
                     relief="solid")  # 567189    413543
    label.place(x=10, y=5)

    # Sensible Heat button
    sensible_heat_btn = tk.Button(main_frame1, text="Sensible Heat", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                  borderwidth=3,
                                  highlightbackground="black", width=17,
                                  bg="#18122b", command=sensible_heat_page)
    sensible_heat_btn.place(x=25, y=70)

    # Latent Heat button
    latent_heat_btn = tk.Button(main_frame1, text="Latent Heat", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                borderwidth=3,
                                highlightbackground="black", width=17,
                                bg="#18122b", command=latent_heat_page)
    latent_heat_btn.place(x=25, y=120)

    # Ideal Gas Law button
    ideal_gas_law_btn = tk.Button(main_frame1, text="Ideal Gas Law", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                  borderwidth=3,
                                  highlightbackground="black", width=17,
                                  bg="#18122b", command=ideal_gas_law_page)
    ideal_gas_law_btn.place(x=25, y=170)

    # Stefan-Boltzmann Law button
    stefan_boltzmann_law_btn = tk.Button(main_frame1, text="Stefan-Boltzmann\nLaw", font=("Verdana", 15), bd=1,
                                         fg="#3A98B9",
                                         borderwidth=3,
                                         highlightbackground="black", width=17,
                                         bg="#18122b", command=stefan_boltzmann_law_page)
    stefan_boltzmann_law_btn.place(x=25, y=220)

    # Thermal Energy button
    thermal_energy_btn = tk.Button(main_frame1, text="Thermal Energy", font=("Verdana", 15), bd=1,
                                   fg="#3A98B9",
                                   borderwidth=3,
                                   highlightbackground="black", width=17,
                                   bg="#18122b", command=thermal_energy_page)
    thermal_energy_btn.place(x=25, y=298)

    # Gibbs free energy button
    gibbs_free_energy_btn = tk.Button(main_frame1, text="Gibbs Free energy", font=("Verdana", 15), bd=1,
                                      fg="#3A98B9",
                                      borderwidth=3,
                                      highlightbackground="black", width=17,
                                      bg="#18122b", command=gibbs_free_energy_page)
    gibbs_free_energy_btn.place(x=25, y=350)

    # Thermodynamic Work button
    thermodynamic_work_btn = tk.Button(main_frame1, text="Thermodynamic\nWork", font=("Verdana", 15), bd=1,
                                       fg="#3A98B9",
                                       borderwidth=3,
                                       highlightbackground="black", width=17,
                                       bg="#18122b", command=thermodynamic_work_page)
    thermodynamic_work_btn.place(x=25, y=400)

    # 1st Law of Thermodynamic button
    first_law_of_thermodynamic_btn = tk.Button(main_frame1, text="First of Law\nThermodynamic", font=("Verdana", 15),
                                               bd=1,
                                               fg="#3A98B9",
                                               borderwidth=3,
                                               highlightbackground="black", width=17,
                                               bg="#18122b", command=first_law_of_thermodynamic_page)
    first_law_of_thermodynamic_btn.place(x=25, y=480)

    # Entropy button
    entropy_btn = tk.Button(main_frame1, text="Entropy", font=("Verdana", 15),
                            bd=1,
                            fg="#3A98B9",
                            borderwidth=3,
                            highlightbackground="black", width=17,
                            bg="#18122b", command=entropy_page)
    entropy_btn.place(x=25, y=560)

    # Thermal efficiency button
    thermal_efficiency_btn = tk.Button(main_frame1, text="Efficiency", font=("Verdana", 15),
                                       bd=1,
                                       fg="#3A98B9",
                                       borderwidth=3,
                                       highlightbackground="black", width=17,
                                       bg="#18122b", command=thermal_efficiency_page)
    thermal_efficiency_btn.place(x=25, y=610)

    # C_O_P button
    c_o_p_btn = tk.Button(main_frame1, text="C.O.P", font=("Verdana", 15),
                          bd=1,
                          fg="#3A98B9",
                          borderwidth=3,
                          highlightbackground="black", width=17,
                          bg="#18122b", command=c_o_p_page)
    c_o_p_btn.place(x=25, y=660)


# Wave and Optics page
def wave_and_optics_page():
    wave_and_optics_frame = tk.Frame(main_frame)
    wave_and_optics_frame.pack()

    # Create a label for Formula
    label = tk.Label(main_frame1, text="FORMULA", font=font1, bg="#3e497a", padx=25, pady=5, width=43, borderwidth=1,
                     relief="solid")  # 567189    413543
    label.place(x=10, y=5)

    # Periodic Waves button
    periodic_waves_btn = tk.Button(main_frame1, text="Periodic Waves", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                   borderwidth=3,
                                   highlightbackground="black", width=17,
                                   bg="#18122b", command=periodic_waves_page)
    periodic_waves_btn.place(x=25, y=70)

    # Beat frequency button
    beat_frequency_btn = tk.Button(main_frame1, text="Beat frequency", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                   borderwidth=3,
                                   highlightbackground="black", width=17,
                                   bg="#18122b", command=beat_frequency_page)
    beat_frequency_btn.place(x=25, y=120)

    # Intensity button
    intensity_btn = tk.Button(main_frame1, text="Intensity", font=("Verdana", 15), bd=1, fg="#3A98B9",
                              borderwidth=3,
                              highlightbackground="black", width=17,
                              bg="#18122b", command=intensity_page)
    intensity_btn.place(x=25, y=170)

    # Sound intensity level button
    sound_intensity_level_btn = tk.Button(main_frame1, text="Intensity level", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                          borderwidth=3,
                                          highlightbackground="black", width=17,
                                          bg="#18122b", command=sound_intensity_level_page)
    sound_intensity_level_btn.place(x=25, y=220)

    # Sound pressure level button
    sound_pressure_level_btn = tk.Button(main_frame1, text="Pressure level", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                         borderwidth=3,
                                         highlightbackground="black", width=17,
                                         bg="#18122b", command=sound_pressure_level_page)
    sound_pressure_level_btn.place(x=25, y=270)

    # Index of Refraction button
    refractive_index_btn = tk.Button(main_frame1, text="Index of Refraction", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                     borderwidth=3,
                                     highlightbackground="black", width=17,
                                     bg="#18122b", command=refractive_index_page)
    refractive_index_btn.place(x=25, y=320)

    # Snell's Law button
    snell_law_btn = tk.Button(main_frame1, text="Snell's Law", font=("Verdana", 15), bd=1, fg="#3A98B9",
                              borderwidth=3,
                              highlightbackground="black", width=17,
                              bg="#18122b", command=snell_law_page)
    snell_law_btn.place(x=25, y=370)

    # Critical Angle button
    critical_angle_btn = tk.Button(main_frame1, text="Critical Angle", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                   borderwidth=3,
                                   highlightbackground="black", width=17,
                                   bg="#18122b", command=critical_angle_page)
    critical_angle_btn.place(x=25, y=420)

    # Focal Length button
    focal_length_btn = tk.Button(main_frame1, text="Focal Length", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                 borderwidth=3,
                                 highlightbackground="black", width=17,
                                 bg="#18122b", command=focal_length_page)
    focal_length_btn.place(x=25, y=470)

    # Magnification button
    magnification_btn = tk.Button(main_frame1, text="Magnification", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                  borderwidth=3,
                                  highlightbackground="black", width=17,
                                  bg="#18122b", command=magnification_page)
    magnification_btn.place(x=25, y=520)

    # Spherical Mirrors button
    spherical_mirrors_btn = tk.Button(main_frame1, text="Spherical Mirrors", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                      borderwidth=3,
                                      highlightbackground="black", width=17,
                                      bg="#18122b", command=spherical_mirrors_page)
    spherical_mirrors_btn.place(x=25, y=570)


# Electricity and Magnetism
def electricity_and_magnetism_page():
    electricity_and_magnetism_frame = tk.Frame(main_frame)
    electricity_and_magnetism_frame.pack()

    # Create a Vertical line in the main frame
    canvas1 = tk.Canvas(main_frame1, width=2, height=800, background="black", bd=-1)
    canvas1.pack()

    # Create a label for Formula
    label = tk.Label(main_frame1, text="FORMULA", font=font1, bg="#3e497a", padx=25, pady=5, width=43, borderwidth=1,
                     relief="solid")  # 567189    413543
    label.place(x=10, y=5)

    # Coulomb's Law button
    coulomb_force_btn = tk.Button(main_frame1, text="Coulomb's Law", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                  borderwidth=3,
                                  highlightbackground="black", width=17,
                                  bg="#18122b", command=coulomb_law_page)
    coulomb_force_btn.place(x=25, y=70)

    # Electric field button
    electric_field_btn = tk.Button(main_frame1, text="Electric field", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                   borderwidth=3,
                                   highlightbackground="black", width=17,
                                   bg="#18122b", command=electric_field_page)
    electric_field_btn.place(x=25, y=120)

    # Electric potential button
    electric_potential_btn = tk.Button(main_frame1, text="Electric Potential", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                       borderwidth=3,
                                       highlightbackground="black", width=17,
                                       bg="#18122b", command=electric_potential_page)
    electric_potential_btn.place(x=25, y=170)

    # Capacitance button
    capacitance_btn = tk.Button(main_frame1, text="Capacitance", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                borderwidth=3,
                                highlightbackground="black", width=17,
                                bg="#18122b", command=capacitance_page)
    capacitance_btn.place(x=25, y=220)

    # Parallel Plate Capacitor button
    parallel_plate_capacitor_btn = tk.Button(main_frame1, text="Parallel Plate\nCapacitor", font=("Verdana", 15), bd=1,
                                             fg="#3A98B9",
                                             borderwidth=3,
                                             highlightbackground="black", width=17,
                                             bg="#18122b", command=parallel_plate_capacitor_page)
    parallel_plate_capacitor_btn.place(x=25, y=270)

    # Electric current button
    electric_current_btn = tk.Button(main_frame1, text="Electric current", font=("Verdana", 15), bd=1,
                                     fg="#3A98B9",
                                     borderwidth=3,
                                     highlightbackground="black", width=17,
                                     bg="#18122b", command=electric_current_page)
    electric_current_btn.place(x=25, y=350)

    # Ohm's Law button
    ohm_law_btn = tk.Button(main_frame1, text="Ohm's Law", font=("Verdana", 15), bd=1,
                            fg="#3A98B9",
                            borderwidth=3,
                            highlightbackground="black", width=17,
                            bg="#18122b", command=ohm_law_page)
    ohm_law_btn.place(x=25, y=400)

    # Electrical Resistance button
    electrical_resistance_btn = tk.Button(main_frame1, text="Electrical Resistance", font=("Verdana", 15), bd=1,
                                          fg="#3A98B9",
                                          borderwidth=3,
                                          highlightbackground="black", width=17,
                                          bg="#18122b", command=electrical_resistance_page)
    electrical_resistance_btn.place(x=25, y=450)

    # Resistors in Series button
    resistors_in_series_btn = tk.Button(main_frame1, text="Resistors in Series", font=("Verdana", 15), bd=1,
                                        fg="#3A98B9",
                                        borderwidth=3,
                                        highlightbackground="black", width=17,
                                        bg="#18122b", command=resistors_in_series_page)
    resistors_in_series_btn.place(x=25, y=500)

    # Resistors in Parallel button
    resistors_in_parallel_btn = tk.Button(main_frame1, text="Resistors in Parallel", font=("Verdana", 15), bd=1,
                                          fg="#3A98B9",
                                          borderwidth=3,
                                          highlightbackground="black", width=17,
                                          bg="#18122b", command=resistors_in_parallel_page)
    resistors_in_parallel_btn.place(x=25, y=550)

    # Capacitors in Series button
    capacitors_in_series_btn = tk.Button(main_frame1, text="Capacitors in Series", font=("Verdana", 15), bd=1,
                                         fg="#3A98B9",
                                         borderwidth=3,
                                         highlightbackground="black", width=17,
                                         bg="#18122b", command=capacitors_in_series_page)
    capacitors_in_series_btn.place(x=25, y=600)

    # Capacitors in Parallel button
    capacitors_in_parallel_btn = tk.Button(main_frame1, text="Capacitors in Parallel", font=("Verdana", 15), bd=1,
                                           fg="#3A98B9",
                                           borderwidth=3,
                                           highlightbackground="black", width=17,
                                           bg="#18122b", command=capacitors_in_parallel_page)
    capacitors_in_parallel_btn.place(x=25, y=650)

    # Magnetic Force(Charge) button
    magnetic_force_btn = tk.Button(main_frame1, text="Magnetic Force\n(Charge)", font=("Verdana", 15), bd=1,
                                   fg="#3A98B9",
                                   borderwidth=3,
                                   highlightbackground="black", width=17,
                                   bg="#18122b", command=magnetic_force_page)
    magnetic_force_btn.place(x=310, y=70)

    # Magnetic Force(Current) button
    magnetic_force1_btn = tk.Button(main_frame1, text="Magnetic Force\n(Current)", font=("Verdana", 15), bd=1,
                                    fg="#3A98B9",
                                    borderwidth=3,
                                    highlightbackground="black", width=17,
                                    bg="#18122b", command=magnetic_force1_page)
    magnetic_force1_btn.place(x=310, y=150)

    # Magnetic Field button
    magnetic_field_btn = tk.Button(main_frame1, text="Biot-Savart Law", font=("Verdana", 15), bd=1,
                                   fg="#3A98B9",
                                   borderwidth=3,
                                   highlightbackground="black", width=17,
                                   bg="#18122b", command=magnetic_field_page)
    magnetic_field_btn.place(x=310, y=230)

    # Solenoid button
    solenoid_btn = tk.Button(main_frame1, text="Solenoid", font=("Verdana", 15), bd=1,
                             fg="#3A98B9",
                             borderwidth=3,
                             highlightbackground="black", width=17,
                             bg="#18122b", command=solenoid_page)
    solenoid_btn.place(x=310, y=280)

    # Straight Wire button
    straight_wire_btn = tk.Button(main_frame1, text="Straight Wire", font=("Verdana", 15), bd=1,
                                  fg="#3A98B9",
                                  borderwidth=3,
                                  highlightbackground="black", width=17,
                                  bg="#18122b", command=straight_wire_page)
    straight_wire_btn.place(x=310, y=330)

    # Parallel Wire button
    parallel_wire_btn = tk.Button(main_frame1, text="Parallel Wire", font=("Verdana", 15), bd=1,
                                  fg="#3A98B9",
                                  borderwidth=3,
                                  highlightbackground="black", width=17,
                                  bg="#18122b", command=parallel_wire_page)
    parallel_wire_btn.place(x=310, y=380)

    # Electric flux button
    electric_flux_btn = tk.Button(main_frame1, text="Electric flux", font=("Verdana", 15), bd=1,
                                  fg="#3A98B9",
                                  borderwidth=3,
                                  highlightbackground="black", width=17,
                                  bg="#18122b", command=electric_flux_page)
    electric_flux_btn.place(x=310, y=430)

    # Magnetic flux button
    magnetic_flux_btn = tk.Button(main_frame1, text="Magnetic flux", font=("Verdana", 15), bd=1,
                                  fg="#3A98B9",
                                  borderwidth=3,
                                  highlightbackground="black", width=17,
                                  bg="#18122b", command=magnetic_flux_page)
    magnetic_flux_btn.place(x=310, y=480)

    # Motional Emf button
    motional_emf_btn = tk.Button(main_frame1, text="Motional Emf", font=("Verdana", 15), bd=1,
                                 fg="#3A98B9",
                                 borderwidth=3,
                                 highlightbackground="black", width=17,
                                 bg="#18122b", command=motional_emf_page)
    motional_emf_btn.place(x=310, y=530)

    # Induced Emf button
    induced_emf_btn = tk.Button(main_frame1, text="Induced Emf", font=("Verdana", 15), bd=1,
                                fg="#3A98B9",
                                borderwidth=3,
                                highlightbackground="black", width=17,
                                bg="#18122b", command=induced_emf_page)
    induced_emf_btn.place(x=310, y=580)

    # Gauss's Law button
    gauss_law_btn = tk.Button(main_frame1, text="Gauss's Law", font=("Verdana", 15), bd=1,
                              fg="#3A98B9",
                              borderwidth=3,
                              highlightbackground="black", width=17,
                              bg="#18122b", command=gauss_law_page)
    gauss_law_btn.place(x=310, y=630)

    # Faraday's Law button
    faraday_law_btn = tk.Button(main_frame1, text="Faraday's Law", font=("Verdana", 15), bd=1,
                                fg="#3A98B9",
                                borderwidth=3,
                                highlightbackground="black", width=17,
                                bg="#18122b", command=faraday_law_page)
    faraday_law_btn.place(x=25, y=700)


# Modern Physics page
def modern_physics_page():
    modern_physics_frame = tk.Frame(main_frame)
    modern_physics_frame.pack()
    # Create a Vertical line in the main frame
    canvas1 = tk.Canvas(main_frame1, width=2, height=800, background="black", bd=-1)
    canvas1.pack()

    # Create a label for Formula
    label = tk.Label(main_frame1, text="FORMULA", font=font1, bg="#3e497a", padx=25, pady=5, width=43, borderwidth=1,
                     relief="solid")  # 567189    413543
    label.place(x=10, y=5)

    # Time Dilation button
    time_dilation_btn = tk.Button(main_frame1, text="Time Dilation", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                  borderwidth=3,
                                  highlightbackground="black", width=17,
                                  bg="#18122b", command=time_dilation_page)
    time_dilation_btn.place(x=25, y=70)

    # Length Contraction button
    length_contraction_btn = tk.Button(main_frame1, text="Length Contraction", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                       borderwidth=3,
                                       highlightbackground="black", width=17,
                                       bg="#18122b", command=length_contraction_page)
    length_contraction_btn.place(x=25, y=120)

    # Relativistic Mass button
    relativistic_mass_btn = tk.Button(main_frame1, text="Relativistic Mass", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                      borderwidth=3,
                                      highlightbackground="black", width=17,
                                      bg="#18122b", command=relativistic_mass_page)
    relativistic_mass_btn.place(x=25, y=170)

    # Relative Velocity button
    relative_velocity_btn = tk.Button(main_frame1, text="Relative Velocity", font=("Verdana", 15), bd=1, fg="#3A98B9",
                                      borderwidth=3,
                                      highlightbackground="black", width=17,
                                      bg="#18122b", command=relative_velocity_page)
    relative_velocity_btn.place(x=25, y=220)

    # Relativistic Momentum button
    relativistic_momentum_btn = tk.Button(main_frame1, text="Relativistic\nMomentum", font=("Verdana", 15), bd=1,
                                          fg="#3A98B9",
                                          borderwidth=3,
                                          highlightbackground="black", width=17,
                                          bg="#18122b", command=relativistic_momentum_page)
    relativistic_momentum_btn.place(x=25, y=270)

    # Energy-Momentum button
    energy_momentum_btn = tk.Button(main_frame1, text="Energy-Momentum", font=("Verdana", 15), bd=1,
                                    fg="#3A98B9",
                                    borderwidth=3,
                                    highlightbackground="black", width=17,
                                    bg="#18122b", command=energy_momentum_page)
    energy_momentum_btn.place(x=25, y=350)

    # Mass-Energy button
    mass_energy_btn = tk.Button(main_frame1, text="Mass-Energy", font=("Verdana", 15), bd=1,
                                fg="#3A98B9",
                                borderwidth=3,
                                highlightbackground="black", width=17,
                                bg="#18122b", command=mass_energy_page)
    mass_energy_btn.place(x=25, y=400)

    # Relativistic Doppler Effect button
    relativistic_doppler_effect_btn = tk.Button(main_frame1, text="Relativistic Doppler\nEffect", font=("Verdana", 15),
                                                bd=1,
                                                fg="#3A98B9",
                                                borderwidth=3,
                                                highlightbackground="black", width=17,
                                                bg="#18122b", command=relativistic_doppler_effect_page)
    relativistic_doppler_effect_btn.place(x=25, y=450)

    # Photon Energy button
    photon_energy_btn = tk.Button(main_frame1, text="Photon Energy", font=("Verdana", 15),
                                  bd=1,
                                  fg="#3A98B9",
                                  borderwidth=3,
                                  highlightbackground="black", width=17,
                                  bg="#18122b", command=photon_energy_page)
    photon_energy_btn.place(x=25, y=530)

    # Half-Life button
    half_life_btn = tk.Button(main_frame1, text="Half-Life", font=("Verdana", 15),
                              bd=1,
                              fg="#3A98B9",
                              borderwidth=3,
                              highlightbackground="black", width=17,
                              bg="#18122b", command=half_life_page)
    half_life_btn.place(x=25, y=580)

    # Photon Momentum button
    photon_momentum_btn = tk.Button(main_frame1, text="Photon Momentum", font=("Verdana", 15),
                                    bd=1,
                                    fg="#3A98B9",
                                    borderwidth=3,
                                    highlightbackground="black", width=17,
                                    bg="#18122b", command=photon_momentum_page)
    photon_momentum_btn.place(x=25, y=630)


# Create option frame
option_frame = tk.Frame(root, bg="#001253")
label2 = tk.Label(option_frame, text="PHYSICS BRANCH", font=font1, bg="grey", padx=25, pady=5, borderwidth=2,
                  relief="solid")
label2.place(x=10, y=50)

# Mechanics button
mechanics_btn = tk.Button(option_frame, text="Mechanics", font=font1, bd=0, fg="#158aff", bg="#c3c3c3", width=18,
                          command=lambda: indicate(mechanics_indicator, mechanics_page))
mechanics_btn.place(x=10, y=100)
mechanics_indicator = tk.Label(option_frame, text="", bg="#c3c3c3")
mechanics_indicator.place(x=3, y=100, width=5, height=40)

# Thermal Physics button
thermal_physics_btn = tk.Button(option_frame, text="Thermal Physics", font=font1, bd=0, fg="#158aff", bg="#c3c3c3",
                                width=18,
                                command=lambda: indicate(thermal_physics_indicator, thermal_physics_page))
thermal_physics_btn.place(x=10, y=150)
thermal_physics_indicator = tk.Label(option_frame, text="", bg="#c3c3c3")
thermal_physics_indicator.place(x=3, y=150, width=5, height=40)

# Wave and Optics button
wave_and_optics_btn = tk.Button(option_frame, text="Wave and Optics", font=font1, bd=0, fg="#158aff", width=18,
                                bg="#c3c3c3",
                                command=lambda: indicate(wave_and_optics_indicator, wave_and_optics_page))
wave_and_optics_btn.place(x=10, y=200)
wave_and_optics_indicator = tk.Label(option_frame, text="", bg="#c3c3c3")
wave_and_optics_indicator.place(x=3, y=200, width=5, height=40)

# Electricity and Magnetism button
electricity_and_magnetism_btn = tk.Button(option_frame, text="Electricity and\nMagnetism", font=font1, bd=0,
                                          fg="#158aff", bg="#c3c3c3", width=18,
                                          command=lambda: indicate(electricity_and_magnetism_indicator,
                                                                   electricity_and_magnetism_page))
electricity_and_magnetism_btn.place(x=10, y=250)
electricity_and_magnetism_indicator = tk.Label(option_frame, text="", bg="#c3c3c3")
electricity_and_magnetism_indicator.place(x=3, y=250, width=5, height=68)

# Modern Physics button
modern_physics_btn = tk.Button(option_frame, text="Modern Physics", font=font1, bd=0, fg="#158aff", width=18,
                               bg="#c3c3c3", command=lambda: indicate(modern_physics_indicator, modern_physics_page))
modern_physics_btn.place(x=10, y=328)
modern_physics_indicator = tk.Label(option_frame, text="", bg="#c3c3c3")
modern_physics_indicator.place(x=3, y=328, width=5, height=40)

# Create option frame
option_frame.pack(side=tk.LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=250, height=10000)

# Create a Horizontal line in the option frame
canvas = tk.Canvas(option_frame, width=250, height=1, bd=0, bg="black")
canvas.place(x=0, y=380)

# Create a Vertical line in the option frame
canvas2 = tk.Canvas(option_frame, width=2, height=800, bd=2, bg="black")
canvas2.place(x=248, y=40)

# Create a Top frame on the top of the option frame
top_frame1 = tk.Frame(option_frame, bg="#191825")
top_frame1.pack(side=tk.TOP)
top_frame1.configure(height=40, width=250)

# Create a Horizontal line in the top frame in the option frame
canvas_top2 = tk.Canvas(top_frame1, width=800, height=1, bd=2, bg="black")
canvas_top2.place(x=0, y=38)

# Create a Vertical line in the top frame
canvas_top = tk.Canvas(top_frame1, width=1, height=40, bd=2, bg="black")
canvas_top.place(x=248, y=0)

# Create a Top frame in the main frame
top_frame = tk.Frame(root, bg="#191825")
top_frame.pack(side=tk.TOP)
top_frame.configure(height=40, width=800)

# Create a Vertical line in the top frame in the main frame
canvas_top2 = tk.Canvas(top_frame, width=800, height=1, bd=-1)
canvas_top2.place(x=-1, y=38)

# Create main frame
main_frame1 = tk.Frame(root, bg="#444654")
main_frame1.pack(side=tk.LEFT)
main_frame1.pack_propagate(False)
main_frame1.configure(height=1000, width=800)
main_frame = tk.Frame(root, bg="black")
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1000, width=800)


# Light mode the toggle section
def toggle_bg():
    current_bg = main_frame1.cget("bg")
    current_bg1 = option_frame.cget("bg")
    if current_bg == "#444654" and current_bg1 == "#001253":
        new_bg = "#f7f7f7"  # ffffff     #f1f6f9
        new_bg1 = "#8ea7e9"
    else:
        new_bg = "#444654"
        new_bg1 = "#001253"
    main_frame1.config(bg=new_bg)
    option_frame.config(bg=new_bg1)


# Create Light and Dark mode button
light_mode = tk.Button(top_frame, text="Change mode", bg="#c3c3c3", font="Arial", command=toggle_bg, bd=-2,
                       borderwidth=1)  # ECF2FF     #e8e2e2     #cddeff
light_mode.place(x=400, y=3)


# Velocity
def calculate_velocity(displacement_entry, time_entry, velocity_label):
    try:
        displacement = float(displacement_entry.get())
        time = float(time_entry.get())
        velocity = displacement / time
        velocity_label.config(text="Velocity = {:.2f} m/s".format(velocity))
    except ValueError:
        velocity_label.config(text="Please enter valid input.")


# Acceleration
def calculate_acceleration(initial_velocity_entry, final_velocity_entry, time_entry, acceleration_label):
    try:
        initial_velocity = float(initial_velocity_entry.get())
        final_velocity = float(final_velocity_entry.get())
        time = float(time_entry.get())
        acceleration = (final_velocity - initial_velocity) / time
        acceleration_label.config(text="Acceleration = {:.2f} m/s²".format(acceleration))
    except ValueError:
        acceleration_label.config(text="Please enter valid input.")


# Calculate Equation of motion
def calculate_equation_of_motion(acceleration1_entry, time2_entry, initial_velocity1_entry, velocity1_label):
    try:
        acceleration1 = float(acceleration1_entry.get())
        time2 = float(time2_entry.get())
        initial_velocity1 = float(initial_velocity1_entry.get())
        velocity1 = (acceleration1 * time2) + initial_velocity1
        velocity1_label.config(text="Velocity = {:.2f} m/s".format(velocity1))
    except ValueError:
        velocity1_label.config(text="Please enter valid input.")


# Calculate Force
def calculate_force(mass_entry, acceleration2_entry, force_label):
    try:
        mass = float(mass_entry.get())
        acceleration2 = float(acceleration2_entry.get())
        force = mass * acceleration2
        force_label.config(text="Force = {:.2f} N".format(force))
    except ValueError:
        force_label.config(text="Please enter valid input.")


# Centripetal acceleration
def calculate_centripetal_acceleration(linear_velocity_entry, radius_entry, centripetal_acceleration_label):
    try:
        linear_velocity = float(linear_velocity_entry.get())
        radius = float(radius_entry.get())
        centripetal_acceleration = linear_velocity ** 2 / radius
        centripetal_acceleration_label.config(
            text="centripetal acceleration = {:.2f} m/s²".format(centripetal_acceleration))
    except ValueError:
        centripetal_acceleration_label.config(text="Please enter valid input.")


# Calculate Momentum
def calculate_momentum(mass_entry, velocity_entry, momentum_label):
    try:
        mass = float(mass_entry.get())
        velocity = float(velocity_entry.get())
        momentum = mass * velocity
        momentum_label.config(text="Force = {:.2f} kgm/s".format(momentum))
    except ValueError:
        momentum_label.config(text="Please enter valid input.")


# Calculate Impulse
def calculate_impulse(force_entry, time_change_entry, impulse_label):
    try:
        force = float(force_entry.get())
        time_change = float(time_change_entry.get())
        impulse = force * time_change
        impulse_label.config(text="Impulse = {:.2f} kgm/s".format(impulse))
    except ValueError:
        impulse_label.config(text="Please enter valid input.")


# Calculate Work
def calculate_work(force_entry, displacement_entry, work_label):
    try:
        force = float(force_entry.get())
        displacement = float(displacement_entry.get())
        work = force * displacement
        work_label.config(text="Work = {:.2f} J".format(work))
    except ValueError:
        work_label.config(text="Please enter valid input.")


# Calculate Kinetic energy
def calculate_kinetic_energy(mass_entry, speed_entry, kinetic_energy_label):
    try:
        mass = float(mass_entry.get())
        speed = float(speed_entry.get())
        kinetic_energy = 0.5 * mass * (speed ** 2)
        kinetic_energy_label.config(text="Kinetic energy = {:.2f} J".format(kinetic_energy))
    except ValueError:
        kinetic_energy_label.config(text="Please enter valid input.")


# Calculate Potential energy
def calculate_potential_energy(mass_entry, height_entry, potential_energy_label):
    try:
        mass = float(mass_entry.get())
        height = float(height_entry.get())
        g = 9.806
        potential_energy = mass * g * height
        potential_energy_label.config(text="Potential energy = {:.2f} J".format(potential_energy))
    except ValueError:
        potential_energy_label.config(text="Please enter valid input.")


# Calculate Efficiency
def calculate_efficiency(net_power_output_entry, heat_flow_rate_entry, efficiency_label):
    try:
        net_power_output = float(net_power_output_entry.get())
        heat_flow_rate = float(heat_flow_rate_entry.get())
        efficiency = net_power_output / heat_flow_rate
        efficiency_label.config(text="Efficiency = {:.2f}".format(efficiency))
    except ValueError:
        efficiency_label.config(text="Please enter valid input.")


# Calculate Power
def calculate_power(work_entry, time_entry, power_label):
    try:
        work = float(work_entry.get())
        time = float(time_entry.get())
        power = work / time
        power_label.config(text="Power = {:.2f} W".format(power))
    except ValueError:
        power_label.config(text="Please enter valid input.")


# Calculate Angular Velocity
def calculate_angular_velocity(linear_velocity_entry, radius_entry, angular_velocity_label):
    try:
        linear_velocity = float(linear_velocity_entry.get())
        radius = float(radius_entry.get())
        angular_velocity = linear_velocity / radius
        angular_velocity_label.config(text="Angular Velocity = {:.2f} rad/s".format(angular_velocity))
    except ValueError:
        angular_velocity_label.config(text="Please enter valid input.")


# Calculate Angular Acceleration
def calculate_angular_acceleration(torque_entry, moment_of_inertia_entry, angular_acceleration_label):
    try:
        torque = float(torque_entry.get())
        moment_of_inertia = float(moment_of_inertia_entry.get())
        angular_acceleration = torque / moment_of_inertia
        angular_acceleration_label.config(text="Angular Acceleration = {:.2f} 1/s²".format(angular_acceleration))
    except ValueError:
        angular_acceleration_label.config(text="Please enter valid input.")


# Calculate Torque
def calculate_torque(force_entry, lever_arm_length_entry, torque_label):
    try:
        force = float(force_entry.get())
        lever_arm_length = float(lever_arm_length_entry.get())
        torque = force * lever_arm_length
        torque_label.config(text="Angular Acceleration = {:.2f} Nm".format(torque))
    except ValueError:
        torque_label.config(text="Please enter valid input.")


# Calculate Moment of Inertia
def calculate_moment_of_inertia(mass_entry, distance_entry, moment_of_inertia_label):
    try:
        mass = float(mass_entry.get())
        distance = float(distance_entry.get())
        moment_of_inertia = mass * (distance ** 2)
        moment_of_inertia_label.config(text="Moment of Inertia = {:.2f} kgm²".format(moment_of_inertia))
    except ValueError:
        moment_of_inertia_label.config(text="Please enter valid input.")


# Calculate Angular Momentum
def calculate_angular_momentum(momentum_of_inertia_entry, distance_entry, angular_momentum_label):
    try:
        momentum_of_inertia = float(momentum_of_inertia_entry.get())
        distance = float(distance_entry.get())
        angular_momentum = momentum_of_inertia * distance
        angular_momentum_label.config(text="Angular Momentum = {:.2f}  Js".format(angular_momentum))
    except ValueError:
        angular_momentum_label.config(text="Please enter valid input.")


# Calculate Universal Gravitation
def calculate_universal_gravitation(first_mass_entry, second_mass_entry, distance_entry, universal_gravitation_label):
    try:
        first_mass = float(first_mass_entry.get())
        second_mass = float(second_mass_entry.get())
        distance = float(distance_entry.get())
        G = 0.667
        force = (G * first_mass * second_mass) / (distance ** 2)
        universal_gravitation_label.config(text="Force = {:.2f} E-10N".format(force))
    except ValueError:
        universal_gravitation_label.config(text="Please enter valid input.")


# Calculate Simple Pendulum(period)
def calculate_period(length_of_string_entry, period_label):
    try:
        length_of_string = float(length_of_string_entry.get())
        pi = 3.14
        g = 9.806
        period = 2 * pi * (math.sqrt(length_of_string) / math.sqrt(g))
        period_label.config(text="Period = {:.2f}  s".format(period))
    except ValueError:
        period_label.config(text="Please enter valid input.")


# Calculate Frequency
def calculate_frequency(period_entry, frequency_label):
    try:
        period = float(period_entry.get())
        frequency = 1 / period
        frequency_label.config(text="Frequency = {:.2f}  Hz".format(frequency))
    except ValueError:
        frequency_label.config(text="Please enter valid input.")


# Calculate Density
def calculate_density(mass_entry, volume_entry, density_label):
    try:
        mass = float(mass_entry.get())
        volume = float(volume_entry.get())
        density = mass / volume
        density_label.config(text="Density = {:.2f}  kg/m³".format(density))
    except ValueError:
        density_label.config(text="Please enter valid input.")


# Calculate Pressure
def calculate_pressure(force_entry, area_entry, pressure_label):
    try:
        force = float(force_entry.get())
        area = float(area_entry.get())
        pressure = force / area
        pressure_label.config(text="Pressure = {:.2f}  pascal".format(pressure))
    except ValueError:
        pressure_label.config(text="Please enter valid input.")


# Calculate Kinematic Viscosity
def calculate_kinematic_viscosity(viscosity_entry, density_entry, kinematic_viscosity_label):
    try:
        viscosity = float(viscosity_entry.get())
        density = float(density_entry.get())
        kinematic_viscosity = viscosity / density
        kinematic_viscosity_label.config(text="Kinematic Viscosity = {:.2f}  m²/s".format(kinematic_viscosity))
    except ValueError:
        kinematic_viscosity_label.config(text="Please enter valid input.")


# Calculate Surface Tension
def calculate_surface_tension(force_entry, length_entry, surface_tension_label):
    try:
        force = float(force_entry.get())
        length = float(length_entry.get())
        surface_tension = 0.5 * (force / length)
        surface_tension_label.config(text="Surface Tension = {:.2f}  N/m".format(surface_tension))
    except ValueError:
        surface_tension_label.config(text="Please enter valid input.")


# Thermal Physics
# Calculate Sensible Heat
def calculate_sensible_heat(mass_entry, specific_heat_capacity_entry, change_in_temperature_entry, sensible_heat_label):
    try:
        mass = float(mass_entry.get())
        specific_heat_capacity = float(specific_heat_capacity_entry.get())
        change_in_temperature = float(change_in_temperature_entry.get())
        sensible_heat = mass * specific_heat_capacity * change_in_temperature
        sensible_heat_label.config(text="Sensible Heat = {:.2f} J".format(sensible_heat))
    except ValueError:
        sensible_heat_label.config(text="Please enter valid input.")


# Calculate Latent Heat
def calculate_latent_heat(mass_entry, specific_latent_heat_entry, latent_heat_label):
    try:
        mass = float(mass_entry.get())
        specific_latent_heat = float(specific_latent_heat_entry.get())
        latent_heat = mass * specific_latent_heat
        latent_heat_label.config(text="Latent Heat = {:.2f}  kJ".format(latent_heat))
    except ValueError:
        latent_heat_label.config(text="Please enter valid input.")


# Calculate Ideal Gas Law
def calculate_ideal_gas_law(volume_entry, amount_of_substance_entry, temperature_entry, pressure_label):
    try:
        volume = float(volume_entry.get())
        amount_of_substance = float(amount_of_substance_entry.get())
        temperature = float(temperature_entry.get())
        R = 8.314
        pressure = amount_of_substance * R * temperature / volume
        pressure_label.config(text="Sensible Heat = {:.2f} N/m²".format(pressure))
    except ValueError:
        pressure_label.config(text="Please enter valid input.")


# Calculate Stefan-Boltzmann Law(Power)
def calculate_power1(area_entry, emissivity_entry, temperature_entry, power_label):
    try:
        area = float(area_entry.get())
        emissivity = float(emissivity_entry.get())
        temperature = float(temperature_entry.get())
        a = 5.67e-8
        power = area * emissivity * a * temperature ** 4
        power_label.config(text="Power = {:.2f} watt".format(power))
    except ValueError:
        power_label.config(text="Please enter valid input.")


# Calculate Thermal Energy
def calculate_thermal_energy(number_of_particles_entry, temperature_entry, thermal_energy_label):
    try:
        number_of_particles = float(number_of_particles_entry.get())
        temperature = float(temperature_entry.get())
        k = 0.138
        thermal_energy = 3 / 2 * number_of_particles * k * temperature
        thermal_energy_label.config(text="Thermal Energy = {:.2f} E-22J".format(thermal_energy))
    except ValueError:
        thermal_energy_label.config(text="Please enter valid input.")


# Calculate Gibbs free energy
def calculate_gibbs_free_energy(enthalpy_entry, temperature_entry, entropy_entry, gibbs_free_energy_label):
    try:
        enthalpy = float(enthalpy_entry.get())
        temperature = float(temperature_entry.get())
        entropy = float(entropy_entry.get())
        gibbs_free_energy = enthalpy - temperature * entropy
        gibbs_free_energy_label.config(text="Gibbs free energy = {:.2f} J".format(gibbs_free_energy))
    except ValueError:
        gibbs_free_energy_label.config(text="Please enter valid input.")


# Calculate Thermodynamic Work
def calculate_thermodynamic_work(pressure_entry, volume_entry, work_label):
    try:
        pressure = float(pressure_entry.get())
        volume = float(volume_entry.get())
        work = pressure * volume
        work_label.config(text="Work = {:.2f}  J".format(work))
    except ValueError:
        work_label.config(text="Please enter valid input.")


# Calculate First Law of Thermodynamic(Internal energy)
def calculate_internal_energy(quantity_of_heat_entry, work_entry, internal_energy_label):
    try:
        quantity_of_heat = float(quantity_of_heat_entry.get())
        work = float(work_entry.get())
        internal_energy = quantity_of_heat - work
        internal_energy_label.config(text="Internal energy = {:.2f}  J".format(internal_energy))
    except ValueError:
        internal_energy_label.config(text="Please enter valid input.")


# Calculate Entropy
def calculate_entropy(quantity_of_heat_entry, temperature_entry, entropy_label):
    try:
        quantity_of_heat = float(quantity_of_heat_entry.get())
        temperature = float(temperature_entry.get())
        entropy = quantity_of_heat / temperature
        entropy_label.config(text="Entropy = {:.2f}  J".format(entropy))
    except ValueError:
        entropy_label.config(text="Please enter valid input.")


# Calculate Efficiency
def calculate_thermal_efficiency(thermal_energy_entry, waste_heat_entry, thermal_efficiency_label):
    try:
        thermal_energy = float(thermal_energy_entry.get())
        waste_heat = float(waste_heat_entry.get())
        thermal_efficiency = 1 - (thermal_energy / waste_heat)
        thermal_efficiency_label.config(text="Thermal efficiency = {:.2f}".format(thermal_efficiency))
    except ValueError:
        thermal_efficiency_label.config(text="Please enter valid input.")


# Calculate C_O_P
def calculate_c_o_p(heat_removed_entry, heat_supplied_entry, c_o_p_label):
    try:
        heat_removed = float(heat_removed_entry.get())
        heat_supplied = float(heat_supplied_entry.get())
        c_o_p = heat_removed / (heat_supplied - heat_removed)
        c_o_p_label.config(text="Coefficient of Perfomance = {:.2f}".format(c_o_p))
    except ValueError:
        c_o_p_label.config(text="Please enter valid input.")


# Calculate Periodic Waves(Phase speed)
def calculate_phase_speed(wavelength_entry, wave_frequency_entry, phase_speed_label):
    try:
        wavelength = float(wavelength_entry.get())
        wave_frequency = float(wave_frequency_entry.get())
        phase_speed = wavelength * wave_frequency
        phase_speed_label.config(text="Phase speed = {:.2f} m/s".format(phase_speed))
    except ValueError:
        phase_speed_label.config(text="Please enter valid input.")


# Calculate Beat frequency
def calculate_beat_frequency(power_radiated_entry, low_frequency_entry, beat_frequency_label):
    try:
        power_radiated = float(power_radiated_entry.get())
        low_frequency = float(low_frequency_entry.get())
        beat_frequency = power_radiated / low_frequency
        beat_frequency_label.config(text="Phase speed = {:.2f} Hz".format(beat_frequency))
    except ValueError:
        beat_frequency_label.config(text="Please enter valid input.")


# Calculate Intensity
def calculate_intensity(power_radiated_entry, area_entry, intensity_label):
    try:
        power_radiated = float(power_radiated_entry.get())
        area = float(area_entry.get())
        intensity = power_radiated / area
        intensity_label.config(text="Intensity = {:.2f} W/m²".format(intensity))
    except ValueError:
        intensity_label.config(text="Please enter valid input.")


# Calculate Intensity Level
def calculate_sound_intensity_level(sound_intensity_entry, reference_intensity_entry, sound_intensity_level_label):
    try:
        sound_intensity = float(sound_intensity_entry.get())
        reference_intensity = float(reference_intensity_entry.get())
        sound_intensity_level = 10 * math.log10(sound_intensity / reference_intensity)
        sound_intensity_level_label.config(text="Sound Intensity Level = {:.2f}".format(sound_intensity_level))
    except ValueError:
        sound_intensity_level_label.config(text="Please enter valid input.")


# Calculate Pressure Level
def calculate_sound_pressure_level(sound_pressure_entry, reference_pressure_entry, sound_pressure_level_label):
    try:
        sound_pressure = float(sound_pressure_entry.get())
        reference_pressure = float(reference_pressure_entry.get())
        sound_pressure_level = 20 * math.log10(sound_pressure / reference_pressure)
        sound_pressure_level_label.config(text="Sound Pressure Level = {:.2f}".format(sound_pressure_level))
    except ValueError:
        sound_pressure_level_label.config(text="Please enter valid input.")


# Calculate Index of Refraction Level
def calculate_refractive_index(phase_velocity_of_light_entry, refractive_index_label):
    try:
        phase_velocity_of_light = float(phase_velocity_of_light_entry.get())
        c = 299792458
        refractive_index = c / phase_velocity_of_light
        refractive_index_label.config(text="Sound Pressure Level = {:.2f}".format(refractive_index))
    except ValueError:
        refractive_index_label.config(text="Please enter valid input.")


# Calculate Snell's Law(Angle of incidence)
def calculate_angle_of_incidence(angle_of_refraction_entry, refractive_index_of_second_medium_entry,
                                 refractive_index_of_first_medium_entry, angle_of_incidence_label, ):
    try:
        angle_of_refraction = float(angle_of_refraction_entry.get())
        refractive_index_of_second_medium = float(refractive_index_of_second_medium_entry.get())
        refractive_index_of_first_medium = float(refractive_index_of_first_medium_entry.get())
        angle_of_incidence = math.asin(
            (refractive_index_of_second_medium / refractive_index_of_first_medium) * math.sin(
                angle_of_refraction))
        print(angle_of_incidence)
        ai = math.degrees(angle_of_incidence)
        angle_of_incidence_label.config(text="Angle of incidence = {:.2f} degree".format(ai))
    except ValueError:
        angle_of_incidence_label.config(text="Please enter valid input.")


# Calculate Snell's Law(Angle of refraction)
def calculate_angle_of_refraction(angle_of_incidence_entry, refractive_index_of_second_medium1_entry,
                                  refractive_index_of_first_medium1_entry, angle_of_refraction_label):
    try:
        angle_of_incidence = float(angle_of_incidence_entry.get())
        refractive_index_of_second_medium1 = float(refractive_index_of_second_medium1_entry.get())
        refractive_index_of_first_medium1 = float(refractive_index_of_first_medium1_entry.get())
        angle_of_refraction = refractive_index_of_second_medium1 / refractive_index_of_first_medium1 * angle_of_incidence
        angle_of_refraction_label.config(text="Angle of refraction = {:.2f} degree".format(angle_of_refraction))
    except ValueError:
        angle_of_refraction_label.config(text="Please enter valid input.")


# Calculate Critical Angle
def calculate_critical_angle(refractive_index_of_second_medium_entry, refractive_index_of_first_medium_entry,
                             critical_angle_label):
    try:
        refractive_index_of_second_medium = float(refractive_index_of_second_medium_entry.get())
        refractive_index_of_first_medium = float(refractive_index_of_first_medium_entry.get())
        critical_angle = refractive_index_of_second_medium / refractive_index_of_first_medium
        critical_angle_label.config(text="Critical Angle = {:.2f} degree".format(critical_angle))
    except ValueError:
        critical_angle_label.config(text="Please enter valid input.")


# Calculate Focal Length
def calculate_focal_length(object_distance_entry, image_distance_entry,
                           focal_length_label):
    try:
        object_distance = float(object_distance_entry.get())
        image_distance = float(image_distance_entry.get())
        f = (1 / object_distance) + (1 / image_distance)
        focal_length = 1 / f
        focal_length_label.config(text="Focal Length = {:.2f} m".format(focal_length))
    except ValueError:
        focal_length_label.config(text="Please enter valid input.")


# Calculate Magnification
def calculate_magnification(object_distance_entry, image_distance_entry,
                            magnification_label):
    try:
        image_distance = float(image_distance_entry.get())
        object_distance = float(object_distance_entry.get())
        magnification = image_distance / object_distance
        magnification_label.config(text="Magnification = {:.2f}".format(magnification))
    except ValueError:
        magnification_label.config(text="Please enter valid input.")


# Calculate Spherical Mirrors(Focal length)
def calculate_focal_length1(radius_of_curvature_entry, focal_length_label):
    try:
        radius_of_curvature = float(radius_of_curvature_entry.get())
        focal_length = radius_of_curvature / 2
        focal_length_label.config(text="Focal Length = {:.2f} m".format(focal_length))
    except ValueError:
        focal_length_label.config(text="Please enter valid input.")


# Electricity and Magnetism
# Calculate Coulomb's Law(Coulomb force)
def calculate_coulomb_force(charge_q1_entry, charge_q2_entry, distance_entry, coulomb_force_label):
    try:
        charge_q1 = float(charge_q1_entry.get())
        charge_q2 = float(charge_q2_entry.get())
        distance = float(distance_entry.get())
        ke = 8.987
        coulomb_force = ke * (charge_q1 * charge_q2 / distance ** 2)
        coulomb_force_label.config(text="Coulomb force = {:.2f} E-9N".format(coulomb_force))
    except ValueError:
        coulomb_force_label.config(text="Please enter valid input.")


# Calculate Electric field
def calculate_electric_field(electrostatic_force_entry, positive_test_charge_entry, electric_field_label):
    try:
        electrostatic_force = float(electrostatic_force_entry.get())
        positive_test_charge = float(positive_test_charge_entry.get())
        electric_field = electrostatic_force / positive_test_charge
        electric_field_label.config(text="Electric field = {:.2f} N/C".format(electric_field))
    except ValueError:
        electric_field_label.config(text="Please enter valid input.")


# Calculate Electric Potential
def calculate_electric_potential(potential_energy_difference_entry, electric_charge_entry, electric_potential_label):
    try:
        potential_energy_difference = float(potential_energy_difference_entry.get())
        electric_charge = float(electric_charge_entry.get())
        electric_potential = potential_energy_difference / electric_charge
        electric_potential_label.config(text="Electric field = {:.2f} V".format(electric_potential))
    except ValueError:
        electric_potential_label.config(text="Please enter valid input.")


# Calculate Capacitance
def calculate_capacitance(electric_charge_entry, potential_difference_entry, capacitance_label):
    try:
        electric_charge = float(electric_charge_entry.get())
        potential_difference = float(potential_difference_entry.get())
        capacitance = electric_charge / potential_difference
        capacitance_label.config(text="Capacitance = {:.2f} F".format(capacitance))
    except ValueError:
        capacitance_label.config(text="Please enter valid input.")


# Calculate Parallel Plate Capacitor
def calculate_capacitance1(permittivity_entry, area_entry, separation_distance_entry, capacitance1_label):
    try:
        permittivity = float(permittivity_entry.get())
        area = float(area_entry.get())
        separation_distance = float(separation_distance_entry.get())
        capacitance1 = permittivity * area / separation_distance
        capacitance1_label.config(text="Capacitance = {:.2f} F".format(capacitance1))
    except ValueError:
        capacitance1_label.config(text="Please enter valid input.")


# Calculate Electric current
def calculate_electric_current(electric_charge_entry, time_entry, electric_current_label):
    try:
        electric_charge = float(electric_charge_entry.get())
        time = float(time_entry.get())
        electric_current = electric_charge / time
        electric_current_label.config(text="Electric current = {:.2f} A".format(electric_current))
    except ValueError:
        electric_current_label.config(text="Please enter valid input.")


# Calculate Ohm's Law(current)
def calculate_current(voltage_entry, resistance_entry, current_label):
    try:
        voltage = float(voltage_entry.get())
        resistance = float(resistance_entry.get())
        current = voltage / resistance
        current_label.config(text="Current = {:.2f} A".format(current))
    except ValueError:
        current_label.config(text="Please enter valid input.")


# Calculate Electrical Resistance
def calculate_resistance(electrical_resistivity_entry, length_of_the_conductor_entry, cross_section_entry,
                         resistance_label):
    try:
        electrical_resistivity = float(electrical_resistivity_entry.get())
        length_of_the_conductor = float(length_of_the_conductor_entry.get())
        cross_section = float(cross_section_entry.get())
        resistance = electrical_resistivity * (length_of_the_conductor / cross_section)
        resistance_label.config(text="Resistance = {:.2f} Ω".format(resistance))
    except ValueError:
        resistance_label.config(text="Please enter valid input.")


# Calculate Resistors in Series(Total resistance)
def calculate_total_resistance(resistance1_entry, resistance2_entry, total_resistance_label):
    try:
        resistance1 = float(resistance1_entry.get())
        resistance2 = float(resistance2_entry.get())
        total_resistance = resistance1 + resistance2
        total_resistance_label.config(text="Total resistance = {:.2f} Ω ".format(total_resistance))
    except ValueError:
        total_resistance_label.config(text="Please enter valid input.")


# Calculate capacitors in Parallel(Total resistance)
def calculate_total_resistance1(resistance1_entry, resistance2_entry, total_resistance1_label):
    try:
        resistance1 = float(resistance1_entry.get())
        resistance2 = float(resistance2_entry.get())
        TR = 1 / resistance1 + 1 / resistance2
        total_resistance1 = 1 / TR
        total_resistance1_label.config(text="Total resistance = {:.2f} Ω ".format(total_resistance1))
    except ValueError:
        total_resistance1_label.config(text="Please enter valid input.")


# Calculate Capacitors in Series(Total resistance)
def calculate_total_capacitance(capacitance1_entry, capacitance2_entry, total_capacitance1_label):
    try:
        capacitance1 = float(capacitance1_entry.get())
        capacitance2 = float(capacitance2_entry.get())
        TC = 1 / capacitance1 + 1 / capacitance2
        total_capacitance1 = 1 / TC
        total_capacitance1_label.config(text="Total capacitance = {:.2f} F ".format(total_capacitance1))
    except ValueError:
        total_capacitance1_label.config(text="Please enter valid input.")


# Calculate Capacitors in Parallel(Total resistance)
def calculate_total_capacitance1(capacitance1_entry, capacitance2_entry, total_capacitance_label):
    try:
        capacitance1 = float(capacitance1_entry.get())
        capacitance2 = float(capacitance2_entry.get())
        total_capacitance = capacitance1 + capacitance2
        total_capacitance_label.config(text="Total capacitance = {:.2f} F ".format(total_capacitance))
    except ValueError:
        total_capacitance_label.config(text="Please enter valid input.")


# Calculate Magnetic Force(Charge)
def calculate_magnetic_force(particle_charge_entry, velocity_of_particle_entry, magnetic_field_entry, angle_entry,
                             magnetic_force_label):
    try:
        particle_charge = float(particle_charge_entry.get())
        velocity_of_particle = float(velocity_of_particle_entry.get())
        magnetic_field = float(magnetic_field_entry.get())
        angle = float(angle_entry.get())
        magnetic_force = particle_charge * velocity_of_particle * magnetic_field * math.sin(angle)
        magnetic_force_label.config(text="Magnetic Force = {:.2f} N ".format(magnetic_force))
    except ValueError:
        magnetic_force_label.config(text="Please enter valid input.")


# Calculate Magnetic Force(Current)
def calculate_magnetic_force0(current_entry, length_entry, magnetic_field_entry, angle_entry,
                              magnetic_force1_label):
    try:
        current = float(current_entry.get())
        length = float(length_entry.get())
        magnetic_field = float(magnetic_field_entry.get())
        angle = float(angle_entry.get())
        magnetic_force = current * length * magnetic_field * math.sin(angle)
        magnetic_force1_label.config(text="Magnetic Force = {:.2f} N ".format(magnetic_force))
    except ValueError:
        magnetic_force1_label.config(text="Please enter valid input.")


# Calculate Magnetic Field
def calculate_magnetic_field(current_entry, length_entry, angle_entry, distance_entry,
                             magnetic_field_label):
    try:
        current = float(current_entry.get())
        length = float(length_entry.get())
        angle = float(angle_entry.get())
        distance = float(distance_entry.get())
        magnetic_field = 10 * (current * length * math.sin(angle) / distance ** 2)
        magnetic_field_label.config(text="Magnetic field = {:.2f} E-8 T ".format(magnetic_field))
    except ValueError:
        magnetic_field_label.config(text="Please enter valid input.")


# Calculate Solenoid(Magnetic Field)
def calculate_magnetic_field0(number_of_loops_entry, current_entry, length_of_the_solenoid_entry,
                              magnetic_field1_label):
    try:
        number_of_loops = float(number_of_loops_entry.get())
        current = float(current_entry.get())
        length_of_the_solenoid = float(length_of_the_solenoid_entry.get())
        mu0 = 4 * 3.14159e-7
        magnetic_field = mu0 * (number_of_loops * current / length_of_the_solenoid)
        magnetic_field1_label.config(text="Magnetic field = {:.2f}  T ".format(magnetic_field))
    except ValueError:
        magnetic_field1_label.config(text="Please enter valid input.")


# Calculate Straight Wire(Magnetic field)
def calculate_magnetic_field1(electric_current_entry, distance_from_the_wire_entry, magnetic_field_label):
    try:
        electric_current = float(electric_current_entry.get())
        distance_from_the_wire = float(distance_from_the_wire_entry.get())
        magnetic_field = 2 * (electric_current / distance_from_the_wire)
        magnetic_field_label.config(text="Magnetic field = {:.6f} E-7T".format(magnetic_field))
    except ValueError:
        magnetic_field_label.config(text="Please enter valid input.")


# Calculate Parallel Wire(Magnetic force)
def calculate_magnetic_force1(current_of_the_wire1_entry, current_of_the_wire2_entry, distance_from_the_wire_entry,
                              magnetic_force_label):
    try:
        current_of_the_wire1 = float(current_of_the_wire1_entry.get())
        current_of_the_wire2 = float(current_of_the_wire2_entry.get())
        distance_from_the_wire = float(distance_from_the_wire_entry.get())
        mu0 = 4 * 3.14159e-7
        magnetic_force = (mu0 * current_of_the_wire1 * current_of_the_wire2) / 2 * math.pi * distance_from_the_wire
        magnetic_force_label.config(text="Magnetic force = {:.5f}E-7  N/m ".format(magnetic_force))
    except ValueError:
        magnetic_force_label.config(text="Please enter valid input.")


# Calculate Electric flux
def calculate_electric_flux(electric_field_entry, surface_area_entry, angle_between_E_and_A_entry,
                            electric_flux_label):
    try:
        electric_field = float(electric_field_entry.get())
        surface_area = float(surface_area_entry.get())
        angle_between_E_and_A = float(angle_between_E_and_A_entry.get())
        electric_flux = electric_field * surface_area * math.cos(angle_between_E_and_A)
        electric_flux_label.config(text="Electric flux = {:.2f}  Vm ".format(electric_flux))
    except ValueError:
        electric_flux_label.config(text="Please enter valid input.")


# Calculate Magnetic flux
def calculate_magnetic_flux(magnetic_field_entry, area_entry, angle_between_B_and_A_entry,
                            magnetic_flux_label):
    try:
        magnetic_field = float(magnetic_field_entry.get())
        area = float(area_entry.get())
        angle_between_B_and_A = float(angle_between_B_and_A_entry.get())
        magnetic_flux = magnetic_field * area * math.cos(angle_between_B_and_A)
        magnetic_flux_label.config(text="Magnetic flux = {:.2f}  Wb ".format(magnetic_flux))
    except ValueError:
        magnetic_flux_label.config(text="Please enter valid input.")


# Calculate Motional Emf
def calculate_motional_emf(magnetic_field_entry, length_entry, velocity_entry,
                           motional_emf_label):
    try:
        magnetic_field = float(magnetic_field_entry.get())
        length = float(length_entry.get())
        velocity = float(velocity_entry.get())
        motional_emf = magnetic_field * length * velocity
        motional_emf_label.config(text="Motional Emf = {:.2f}  V ".format(motional_emf))
    except ValueError:
        motional_emf_label.config(text="Please enter valid input.")


# Calculate Induced Emf
def calculate_induced_emf(magnetic_flux_entry, time_entry, induced_emf_label):
    try:
        magnetic_flux = float(magnetic_flux_entry.get())
        time = float(time_entry.get())
        induced_emf = - (magnetic_flux / time)
        induced_emf_label.config(text="Induced Emf = {:.2f}  V ".format(induced_emf))
    except ValueError:
        induced_emf_label.config(text="Please enter valid input.")


# Calculate Gauss's Law(Electric flux)
def calculate_electric_flux1(total_charge_entry, electric_flux1_label):
    global convert_ef
    try:
        total_charge = float(total_charge_entry.get())
        E0 = 8.854e-12
        if 1 <= total_charge <= 8:
            electric_flux = total_charge / E0
            convert_ef = f"Electric flux = {electric_flux / 10 ** 11:.2f}E11 Wb"
        elif 8 < total_charge <= 88:
            electric_flux = total_charge / E0
            convert_ef = f"Electric flux = {electric_flux / 10 ** 12:.2f}E12 Wb"
        elif 88 < total_charge <= 880:
            electric_flux = total_charge / E0
            convert_ef = f"Electric flux = {electric_flux / 10 ** 13:.2f}E13 Wb"
        elif 880 < total_charge <= 8809:
            electric_flux = total_charge / E0
            convert_ef = f"Electric flux = {electric_flux / 10 ** 14:.2f}E14 Wb"
        elif 8809 < total_charge <= 88090:
            electric_flux = total_charge / E0
            convert_ef = f"Electric flux = {electric_flux / 10 ** 15:.2f}E15 Wb"
        elif 88090 < total_charge <= 880991:
            electric_flux = total_charge / E0
            convert_ef = f"Electric flux = {electric_flux / 10 ** 16:.2f}E16 Wb"
        else:
            electric_flux = total_charge / E0
            convert_ef = f"Electric flux = {electric_flux / 10 ** 17:.2f}E17 Wb"
        electric_flux1_label.config(text=convert_ef.format(convert_ef))
    except ValueError:
        electric_flux1_label.config(text="Please enter valid input.")


# Calculate Faraday's Law(Induced Emf)
def calculate_induced_emf1(magnetic_flux_entry, time_entry, induced_emf1_label):
    try:
        magnetic_flux = float(magnetic_flux_entry.get())
        time = float(time_entry.get())
        induced_emf1 = - (magnetic_flux / time)
        induced_emf1_label.config(text="Induced Emf = {:.2f}  V ".format(induced_emf1))
    except ValueError:
        induced_emf1_label.config(text="Please enter valid input.")


# Modern Physics
# Calculate Time Dilation(Time between same events)
def calculate_time_between_same_events(time_between_2_colocal_events_entry, velocity_entry,
                                       time_between_same_events_label):
    try:
        time_between_2_colocal_events = float(time_between_2_colocal_events_entry.get())
        velocity = float(velocity_entry.get())
        c = 299792458
        time_between_same_events = time_between_2_colocal_events / math.sqrt(1 - velocity ** 2 / c ** 2)
        time_between_same_events_label.config(
            text="Time between\nsame events = {:.2f}  s ".format(time_between_same_events))
    except ValueError:
        time_between_same_events_label.config(text="Please enter valid input.")


# Calculate Length Contraction(Length observed)
def calculate_length_observed(proper_length_entry, relative_velocity_entry,
                              length_observed_label):
    try:
        proper_length = float(proper_length_entry.get())
        relative_velocity = float(relative_velocity_entry.get())
        c = 299792458
        length_observed = proper_length * math.sqrt(1 - (relative_velocity ** 2 / c ** 2))
        length_observed_label.config(text="Length Observed = {:.2f}  m ".format(length_observed))
    except ValueError:
        length_observed_label.config(text="Please enter valid input.")


# Calculate Relativistic Mass
def calculate_relativistic_mass(rest_mass, velocity_entry, relativistic_mass_label):
    try:
        rest_mass = float(rest_mass.get())
        velocity = float(velocity_entry.get())
        c = 299792458
        relativistic_mass = rest_mass / math.sqrt(1 - (velocity ** 2 / c ** 2))
        relativistic_mass_label.config(text="Relativistic Mass= {:.2f}  kg ".format(relativistic_mass))
    except ValueError:
        relativistic_mass_label.config(text="Please enter valid input.")


# Calculate Relative Velocity
def calculate_relative_velocity(velocity_of_a, velocity_of_b_entry, relative_velocity_label):
    try:
        velocity_of_a = float(velocity_of_a.get())
        velocity_of_b = float(velocity_of_b_entry.get())
        c = 299792458
        relative_velocity = velocity_of_a + velocity_of_b / 1 + (velocity_of_a * velocity_of_b / c)
        relative_velocity_label.config(text="Relative Velocity= {:.2f}  m/s ".format(relative_velocity))
    except ValueError:
        relative_velocity_label.config(text="Please enter valid input.")


# Calculate Relativistic Momentum
def calculate_relativistic_momentum(mass, velocity_entry, relativistic_momentum_label):
    try:
        mass = float(mass.get())
        velocity = float(velocity_entry.get())
        c = 299792458
        relativistic_momentum = mass * velocity / math.sqrt(1 - (velocity ** 2 / c ** 2))
        relativistic_momentum_label.config(text="Relativistic Momentum = {:.2f}  kgm/s ".format(relativistic_momentum))
    except ValueError:
        relativistic_momentum_label.config(text="Please enter valid input.")


# Calculate Energy-Momentum
def calculate_energy_momentum(momentum, rest_mass_entry, energy_momentum_label):
    try:
        momentum = float(momentum.get())
        rest_mass = float(rest_mass_entry.get())
        c = 299792458
        energy_momentum = (momentum ** 2) * (c ** 2) + (rest_mass ** 2) * (c ** 4)
        em = math.sqrt(energy_momentum)
        convert_em = f"Energy = {em / 10 ** 17:.2f}E17 J"
        energy_momentum_label.config(text=convert_em.format(convert_em))
    except ValueError:
        energy_momentum_label.config(text="Please enter valid input.")


# Calculate Mass-Energy
def calculate_mass_energy(mass_entry, mass_energy_label):
    global convert_me
    try:
        mass = float(mass_entry.get())
        c = 299792458
        if mass <= 11:
            mass_energy = mass * (c ** 2)
            convert_me = f"Energy = {mass_energy / 10 ** 17:.2f}E17 J"
        elif 11 < mass <= 110:
            mass_energy = mass * (c ** 2)
            convert_me = f"Energy = {mass_energy / 10 ** 18:.2f}E18 J"
        elif 110 < mass <= 1107:
            mass_energy = mass * (c ** 2)
            convert_me = f"Energy = {mass_energy / 10 ** 19:.2f}E19 J"
        elif 1108 < mass <= 11070:
            mass_energy = mass * (c ** 2)
            convert_me = f"Energy = {mass_energy / 10 ** 20:.2f}E20 J"
        elif 11070 < mass <= 110708:
            mass_energy = mass * (c ** 2)
            convert_me = f"Energy = {mass_energy / 10 ** 21:.2f}E21 J"
        else:
            mass_energy = mass * (c ** 2)
            convert_me = f"Energy = {mass_energy / 10 ** 22:.2f}E22 J"
        mass_energy_label.config(text=convert_me.format(convert_me))
    except ValueError:
        mass_energy_label.config(text="Please enter valid input.")


# Calculate Relativistic Doppler Effect(Perceived Wavelength)
def calculate_perceived_wavelength(wavelength_entry, velocity_entry, perceived_wavelength_label):
    try:
        wavelength = float(wavelength_entry.get())
        velocity = float(velocity_entry.get())
        c = 299792458
        perceived_wavelength = math.sqrt(1 + (velocity / c) / (1 - (velocity / c))) * wavelength
        perceived_wavelength_label.config(text="Perceived Wavelength = {:.3f}  m ".format(perceived_wavelength))
    except ValueError:
        perceived_wavelength_label.config(text="Please enter valid input.")


# Calculate Photon Energy
def calculate_photon_energy(frequency_entry, photon_energy_label):
    global convert_pe
    try:
        frequency = float(frequency_entry.get())
        h = 6.626e-34
        if frequency == 1:
            photon_energy = h * frequency
            convert_pe = f"Photon Energy = {photon_energy / 10 ** -34:.2f}E-34 J"
        elif 1 < frequency <= 15:
            photon_energy = h * frequency
            convert_pe = f"Photon Energy = {photon_energy / 10 ** -33:.2f}E-33 J"
        elif 15 < frequency <= 150:
            photon_energy = h * frequency
            convert_pe = f"Photon Energy = {photon_energy / 10 ** -32:.2f}E-32 J"
        elif 150 < frequency <= 1501:
            photon_energy = h * frequency
            convert_pe = f"Photon Energy = {photon_energy / 10 ** -31:.2f}E-31 J"
        elif 1501 < frequency <= 15016:
            photon_energy = h * frequency
            convert_pe = f"Photon Energy = {photon_energy / 10 ** -30:.2f}E-30 J"
        elif 15016 < frequency <= 150164:
            photon_energy = h * frequency
            convert_pe = f"Photon Energy = {photon_energy / 10 ** -29:.2f}E-29 J"
        else:
            photon_energy = h * frequency
            convert_pe = f"Photon Energy = {photon_energy / 10 ** -28:.2f}E-28 J"
        photon_energy_label.config(text=convert_pe.format(convert_pe))
    except ValueError:
        photon_energy_label.config(text="Please enter valid input.")


# Calculate Half-Life
def calculate_half_life(decay_constant_entry, half_life_label):
    try:
        decay_constant = float(decay_constant_entry.get())
        ln2 = 0.69314718056
        half_life = ln2 / decay_constant
        half_life_label.config(text="Half-Life = {:.3f}".format(half_life))
    except ValueError:
        half_life_label.config(text="Please enter valid input.")


# Calculate Photon Momentum
def calculate_momentum_of_the_photon(wavelength, momentum_of_the_photon_label):
    global convert_mp
    try:
        wavelength = float(wavelength.get())
        h = 6.626e-34
        if wavelength <= 6:
            momentum_of_the_photon = h / wavelength
            convert_mp = f"Momentum of the photon = {momentum_of_the_photon / 10 ** -34:.2f}E-34 kgm/s"
        elif 6 < wavelength <= 66:
            momentum_of_the_photon = h / wavelength
            convert_mp = f"Momentum of the photon = {momentum_of_the_photon / 10 ** -35:.2f}E-35 kgm/s"
        elif 66 < wavelength <= 665:
            momentum_of_the_photon = h / wavelength
            convert_mp = f"Momentum of the photon = {momentum_of_the_photon / 10 ** -36:.2f}E-36 kgm/s"
        elif 665 < wavelength <= 6659:
            momentum_of_the_photon = h / wavelength
            convert_mp = f"Momentum of the photon = {momentum_of_the_photon / 10 ** -37:.2f}E-37 kgm/s"
        elif 6659 < wavelength <= 66593:
            momentum_of_the_photon = h / wavelength
            convert_mp = f"Momentum of the photon = {momentum_of_the_photon / 10 ** -38:.2f}E-38 kgm/s"
        else:
            momentum_of_the_photon = h / wavelength
            convert_mp = f"Momentum of the photon = {momentum_of_the_photon / 10 ** -39:.2f}E-39 kgm/s"
        momentum_of_the_photon_label.config(text=convert_mp.format(convert_mp))
    except ValueError:
        momentum_of_the_photon_label.config(text="Please enter valid input.")


# Velocity
def clear(displacement_entry, time_entry):
    displacement_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)


# Acceleration
def clear1(initial_velocity_entry, final_velocity_entry, time1_entry):
    initial_velocity_entry.delete(0, tk.END)
    final_velocity_entry.delete(0, tk.END)
    time1_entry.delete(0, tk.END)


# Equation of motion
def clear2(initial_velocity1_entry, acceleration1_entry, time2_entry):
    initial_velocity1_entry.delete(0, tk.END)
    acceleration1_entry.delete(0, tk.END)
    time2_entry.delete(0, tk.END)


# Force
def clear3(mass_entry, acceleration2_entry):
    mass_entry.delete(0, tk.END)
    acceleration2_entry.delete(0, tk.END)


# Centripetal acceleration
def clear4(linear_velocity_entry, radius_entry):
    linear_velocity_entry.delete(0, tk.END)
    radius_entry.delete(0, tk.END)


# Momentum
def clear5(mass_entry, velocity_entry):
    mass_entry.delete(0, tk.END)
    velocity_entry.delete(0, tk.END)


# Impulse
def clear6(force_entry, time_change_entry):
    force_entry.delete(0, tk.END)
    time_change_entry.delete(0, tk.END)


# Work clear button
def clear7(force_entry, displacement_entry):
    force_entry.delete(0, tk.END)
    displacement_entry.delete(0, tk.END)


# Kinetic energy clear button
def clear8(mass_entry, speed_entry):
    mass_entry.delete(0, tk.END)
    speed_entry.delete(0, tk.END)


# Potential energy clear button
def clear9(mass_entry, height_entry):
    mass_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
   

# Efficiency clear button
def clear10(net_power_output_entry, heat_flow_rate_entry):
    net_power_output_entry.delete(0, tk.END)
    heat_flow_rate_entry.delete(0, tk.END)


# Power clear button
def clear11(work_entry, time_entry):
    work_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)


# Angular Velocity clear button
def clear12(linear_velocity_entry, radius_entry):
    linear_velocity_entry.delete(0, tk.END)
    radius_entry.delete(0, tk.END)


# Angular Acceleration clear button
def clear13(torque_entry, moment_of_inertia_entry):
    torque_entry.delete(0, tk.END)
    moment_of_inertia_entry.delete(0, tk.END)


# Torque clear button
def clear14(force_entry, lever_arm_length_entry):
    force_entry.delete(0, tk.END)
    lever_arm_length_entry.delete(0, tk.END)


# Moment of Inertia clear button
def clear15(mass_entry, distance_entry):
    mass_entry.delete(0, tk.END)
    distance_entry.delete(0, tk.END)


# Angular Momentum clear button
def clear16(momentum_of_inertia_entry, distance_entry):
    momentum_of_inertia_entry.delete(0, tk.END)
    distance_entry.delete(0, tk.END)


# Universal Momentum clear button
def clear17(first_mass_entry, second_mass_entry, distance_entry):
    first_mass_entry.delete(0, tk.END)
    second_mass_entry.delete(0, tk.END)
    distance_entry.delete(0, tk.END)


# Simple Pendulum clear button
def clear18(length_of_string_entry):
    length_of_string_entry.delete(0, tk.END)


# Frequency clear button
def clear19(period_entry):
    period_entry.delete(0, tk.END)


# Density clear button
def clear20(mass_entry, volume_entry):
    mass_entry.delete(0, tk.END)
    volume_entry.delete(0, tk.END)


# Pressure clear button
def clear21(force_entry, area_entry):
    force_entry.delete(0, tk.END)
    area_entry.delete(0, tk.END)


# Kinematic Viscosity clear button
def clear22(viscosity_entry, density_entry):
    viscosity_entry.delete(0, tk.END)
    density_entry.delete(0, tk.END)


# Surface Tension clear button
def clear23(force_entry, length_entry):
    force_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)


# Thermal Physics
# Surface Tension clear button
def clear24(mass_entry, specific_heat_capacity_entry, change_in_temperature_entry):
    mass_entry.delete(0, tk.END)
    specific_heat_capacity_entry.delete(0, tk.END)
    change_in_temperature_entry.delete(0, tk.END)


# Surface Tension clear button
def clear25(mass_entry, specific_latent_heat_entry):
    mass_entry.delete(0, tk.END)
    specific_latent_heat_entry.delete(0, tk.END)


# Surface Tension clear button
def clear26(volume_entry, amount_of_substance_entry, temperature_entry):
    volume_entry.delete(0, tk.END)
    amount_of_substance_entry.delete(0, tk.END)
    temperature_entry.delete(0, tk.END)


# Stefan-Boltzmann Law clear button
def clear27(area_entry, emissivity_entry, temperature_entry):
    area_entry.delete(0, tk.END)
    emissivity_entry.delete(0, tk.END)
    temperature_entry.delete(0, tk.END)


# Thermal Energy clear button
def clear28(number_of_particles_entry, temperature_entry):
    number_of_particles_entry.delete(0, tk.END)
    temperature_entry.delete(0, tk.END)


# Gibbs free energy clear button
def clear29(enthalpy_entry, temperature_entry, entropy_entry):
    enthalpy_entry.delete(0, tk.END)
    temperature_entry.delete(0, tk.END)
    entropy_entry.delete(0, tk.END)


# Thermodynamic Work clear button
def clear30(pressure_entry, volume_entry):
    pressure_entry.delete(0, tk.END)
    volume_entry.delete(0, tk.END)


# 1st Law of Thermodynamic clear button
def clear31(quantity_of_heat_entry, work_entry):
    quantity_of_heat_entry.delete(0, tk.END)
    work_entry.delete(0, tk.END)


# Entropy clear button
def clear32(quantity_of_heat_entry, temperature_entry):
    quantity_of_heat_entry.delete(0, tk.END)
    temperature_entry.delete(0, tk.END)


# Efficiency clear button
def clear33(thermal_energy_entry, waste_heat_entry):
    thermal_energy_entry.delete(0, tk.END)
    waste_heat_entry.delete(0, tk.END)


# C_O_P clear button
def clear34(heat_removed_entry, heat_supplied_entry):
    heat_removed_entry.delete(0, tk.END)
    heat_supplied_entry.delete(0, tk.END)


# Periodic Waves clear button
def clear35(wavelength_entry, wave_frequency_entry):
    wavelength_entry.delete(0, tk.END)
    wave_frequency_entry.delete(0, tk.END)


# Beat frequency clear button
def clear36(high_frequency_entry, low_frequency_entry):
    high_frequency_entry.delete(0, tk.END)
    low_frequency_entry.delete(0, tk.END)


# Intensity clear button
def clear37(power_radiated_entry, area_entry):
    power_radiated_entry.delete(0, tk.END)
    area_entry.delete(0, tk.END)


# Intensity Level clear button
def clear38(sound_intensity_entry, reference_intensity_entry):
    sound_intensity_entry.delete(0, tk.END)
    reference_intensity_entry.delete(0, tk.END)


# Pressure Level clear button
def clear39(sound_pressure_entry, reference_pressure_entry):
    sound_pressure_entry.delete(0, tk.END)
    reference_pressure_entry.delete(0, tk.END)


# Index of Refraction clear button
def clear40(phase_velocity_of_light_entry):
    phase_velocity_of_light_entry.delete(0, tk.END)


# Angle of incidence clear button
def clear41a(angle_of_refraction_entry, refractive_index_of_second_medium_entry,
             refractive_index_of_first_medium_entry):
    angle_of_refraction_entry.delete(0, tk.END)
    refractive_index_of_second_medium_entry.delete(0, tk.END)
    refractive_index_of_first_medium_entry.delete(0, tk.END)


# Angle of incidence clear button
def clear41b(angle_of_incidence_entry, refractive_index_of_second_medium1_entry,
             refractive_index_of_first_medium1_entry):
    angle_of_incidence_entry.delete(0, tk.END)
    refractive_index_of_second_medium1_entry.delete(0, tk.END)
    refractive_index_of_first_medium1_entry.delete(0, tk.END)


# Critical Angle clear button
def clear42(refractive_index_of_second_medium_entry, refractive_index_of_first_medium_entry):
    refractive_index_of_second_medium_entry.delete(0, tk.END)
    refractive_index_of_first_medium_entry.delete(0, tk.END)


# Focal Length clear button
def clear43(object_distance_entry, image_distance_entry):
    object_distance_entry.delete(0, tk.END)
    image_distance_entry.delete(0, tk.END)


# Magnification clear button
def clear44(object_distance_entry, image_distance_entry):
    object_distance_entry.delete(0, tk.END)
    image_distance_entry.delete(0, tk.END)


# Magnification clear button
def clear45(radius_of_curvature_entry):
    radius_of_curvature_entry.delete(0, tk.END)


# Electricity and Magnetism
# Angle of incidence clear button
def clear46(charge_q1_entry, charge_q2_entry, distance_entry):
    charge_q1_entry.delete(0, tk.END)
    charge_q2_entry.delete(0, tk.END)
    distance_entry.delete(0, tk.END)


# Electric field clear button
def clear47(electrostatic_force_entry, positive_test_charge_entry):
    electrostatic_force_entry.delete(0, tk.END)
    positive_test_charge_entry.delete(0, tk.END)


# Electric Potential clear button
def clear48(potential_energy_difference_entry, electric_charge_entry):
    potential_energy_difference_entry.delete(0, tk.END)
    electric_charge_entry.delete(0, tk.END)


# Capacitance clear button
def clear49(electric_charge_entry, potential_difference_entry):
    electric_charge_entry.delete(0, tk.END)
    potential_difference_entry.delete(0, tk.END)


# Angle of incidence clear button
def clear50(permittivity_entry, area_entry, separation_distance_entry):
    permittivity_entry.delete(0, tk.END)
    area_entry.delete(0, tk.END)
    separation_distance_entry.delete(0, tk.END)


# Electric current clear button
def clear51(electric_charge_entry, time_entry):
    electric_charge_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)


# Electric current clear button
def clear52(voltage_entry, resistance_entry):
    voltage_entry.delete(0, tk.END)
    resistance_entry.delete(0, tk.END)


# Electrical Resistance clear button
def clear53(electrical_resistivity_entry, length_of_the_conductor_entry, cross_section_entry):
    electrical_resistivity_entry.delete(0, tk.END)
    length_of_the_conductor_entry.delete(0, tk.END)
    cross_section_entry.delete(0, tk.END)


# Resistors in Series clear button
def clear54(resistance1_entry, resistance2_entry):
    resistance1_entry.delete(0, tk.END)
    resistance2_entry.delete(0, tk.END)


# Resistors in Parallel clear button
def clear55(resistance1_entry, resistance2_entry):
    resistance1_entry.delete(0, tk.END)
    resistance2_entry.delete(0, tk.END)


# Capacitors in Series clear button
def clear56(capacitance1_entry, capacitance2_entry):
    capacitance1_entry.delete(0, tk.END)
    capacitance2_entry.delete(0, tk.END)


# Capacitors in Parallel clear button
def clear57(capacitance1_entry, capacitance2_entry):
    capacitance1_entry.delete(0, tk.END)
    capacitance2_entry.delete(0, tk.END)


# Magnetic Force(Charge) clear button
def clear58(particle_charge_entry, velocity_of_particle_entry, magnetic_field_entry, angle_entry):
    particle_charge_entry.delete(0, tk.END)
    velocity_of_particle_entry.delete(0, tk.END)
    magnetic_field_entry.delete(0, tk.END)
    angle_entry.delete(0, tk.END)


# Magnetic Force(Current) clear button
def clear59(current_entry, length_entry, magnetic_field_entry, angle_entry):
    current_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    magnetic_field_entry.delete(0, tk.END)
    angle_entry.delete(0, tk.END)


# Magnetic Field clear button
def clear60(current_entry, length_entry, angle_entry, distance_entry):
    current_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    angle_entry.delete(0, tk.END)
    distance_entry.delete(0, tk.END)


# Solenoid(Magnetic Field) clear button
def clear61(number_of_loops_entry, current_entry, length_of_the_solenoid_entry):
    number_of_loops_entry.delete(0, tk.END)
    current_entry.delete(0, tk.END)
    length_of_the_solenoid_entry.delete(0, tk.END)


# Straight Wire(Magnetic Field) clear button
def clear62(electric_current_entry, distance_from_the_wire_entry, ):
    electric_current_entry.delete(0, tk.END)
    distance_from_the_wire_entry.delete(0, tk.END)


# Parallel Wire(Magnetic force) clear button
def clear63(current_of_the_wire1_entry, current_of_the_wire2_entry, distance_from_the_wire_entry):
    current_of_the_wire1_entry.delete(0, tk.END)
    current_of_the_wire2_entry.delete(0, tk.END)
    distance_from_the_wire_entry.delete(0, tk.END)


# Electric flux clear button
def clear64(electric_field_entry, surface_area_entry, angle_between_E_and_A_entry):
    electric_field_entry.delete(0, tk.END)
    surface_area_entry.delete(0, tk.END)
    angle_between_E_and_A_entry.delete(0, tk.END)


# Magnetic flux clear button
def clear65(magnetic_field_entry, area_entry, angle_between_B_and_A_entry):
    magnetic_field_entry.delete(0, tk.END)
    area_entry.delete(0, tk.END)
    angle_between_B_and_A_entry.delete(0, tk.END)


# Motional Emf clear button
def clear66(magnetic_field_entry, length_entry, velocity_entry):
    magnetic_field_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    velocity_entry.delete(0, tk.END)


# Induced Emf clear button
def clear67(magnetic_flux_entry, time_entry):
    magnetic_flux_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)


# Gauss's Law clear button
def clear68(total_charge_entry):
    total_charge_entry.delete(0, tk.END)


# Faraday's Law(Induced Emf) clear button
def clear69(magnetic_flux_entry, time_entry):
    magnetic_flux_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)


# Time Dilation clear button
def clear70(time_between_2_colocal_events_entry, velocity_entry):
    time_between_2_colocal_events_entry.delete(0, tk.END)
    velocity_entry.delete(0, tk.END)


# Length Contraction clear button
def clear71(proper_length_entry, relative_velocity_entry):
    proper_length_entry.delete(0, tk.END)
    relative_velocity_entry.delete(0, tk.END)


# Relativistic Mass clear button
def clear72(rest_mass_entry, velocity_entry):
    rest_mass_entry.delete(0, tk.END)
    velocity_entry.delete(0, tk.END)


# Relative Velocity clear button
def clear73(velocity_of_a_entry, velocity_of_b_entry):
    velocity_of_a_entry.delete(0, tk.END)
    velocity_of_b_entry.delete(0, tk.END)


# Relativistic Momentum clear button
def clear74(mass_entry, velocity_entry):
    mass_entry.delete(0, tk.END)
    velocity_entry.delete(0, tk.END)


# Energy-Momentum clear button
def clear75(momentum_entry, rest_mass_entry):
    momentum_entry.delete(0, tk.END)
    rest_mass_entry.delete(0, tk.END)


# Mass-Energy clear button
def clear76(mass_entry):
    mass_entry.delete(0, tk.END)


# Energy-Momentum clear button
def clear77(wavelength_entry, velocity_entry):
    wavelength_entry.delete(0, tk.END)
    velocity_entry.delete(0, tk.END)


# Photon Energy clear button
def clear78(frequency_entry):
    frequency_entry.delete(0, tk.END)


# Half-Life clear button
def clear79(decay_constant_entry):
    decay_constant_entry.delete(0, tk.END)


# Photon Momentum clear button
def clear80(wavelength_entry):
    wavelength_entry.delete(0, tk.END)


root.mainloop()
