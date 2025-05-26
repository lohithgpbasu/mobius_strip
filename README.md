# Möbius Strip Generator 🌀

This Python project models a 3D Möbius Strip using parametric equations and calculates its **surface area** and **edge length** using numerical methods.

---

## 🚀 Features

- Parametric 3D model of a Möbius strip  
- Approximate **surface area** using cross product of vectors  
- Approximate **edge length** using Euclidean distance  
- Interactive 3D visualization with `matplotlib`

---

## 📦 Requirements

Install the required Python modules using:

```bash
pip install numpy matplotlib
```

---

## 📁 File Structure

- cd mobius_strip
  - mobius_strip.py
  - README.md

---

## 🧠 How It Works

Parametric Equations:

- x(u,v)=(R+v∗cos(u/2))∗cos(u)y(u,v)=(R+v∗cos(u/2))∗sin(u)z(u,v)=v∗sin(u/2)

Where:

```bash
  u ∈ [0, 2π]
  v ∈ [-w/2, w/2]
```

Core Functions:

- surface_area() – Uses tiny 3D triangles (via cross product) to estimate total surface area.

- edge_length() – Adds distances along both edges to estimate boundary length.

- plot() – Visualizes the strip in 3D.

---

## 💉 Usage

```bash
python mobius_strip.py
```

---

## You'll see

- Printed surface area and edge length.
- A 3D plot of the Möbius strip.

---

## Structure

- One class MobiusStrip with methods to compute mesh, surface area, edge length, and visualization.
- Modular functions to keep it clean and readable.

## Approach to Surface Area

- Used finite difference method to approximate partial derivatives.
- Computed area of tiny parallelograms using cross product.
- Summed over mesh grid to get total surface area.

## Challenges

- Keeping numerical stability at high resolutions.
- Balancing speed vs. accuracy in surface_area().

---

## Images

- Input Image.

![Input Image](https://res.cloudinary.com/djyotwnhe/image/upload/v1748279727/Screenshot_2025-05-26_215446_ootjbe.png)

- Mobius Plot.

![Möbius Plot](https://res.cloudinary.com/djyotwnhe/image/upload/v1748279761/Screenshot_2025-05-26_213701_vtgvuw.png)
