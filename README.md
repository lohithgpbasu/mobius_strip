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
- ```bash
  u ∈ [0, 2π]