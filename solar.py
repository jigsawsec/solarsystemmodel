# Define the positions and sizes of the planets (in astronomical units, AU)
# Approximate distances from the Sun and relative sizes
planets = {
    'Sun': {'distance': 0, 'size': 0.1, 'color': 'yellow'},
    'Mercury': {'distance': 0.39, 'size': 0.02, 'color': 'gray'},
    'Venus': {'distance': 0.72, 'size': 0.05, 'color': 'orange'},
    'Earth': {'distance': 1.00, 'size': 0.05, 'color': 'blue'},
    'Mars': {'distance': 1.52, 'size': 0.03, 'color': 'red'},
    'Jupiter': {'distance': 5.20, 'size': 0.1, 'color': 'brown'},
    'Saturn': {'distance': 9.58, 'size': 0.09, 'color': 'goldenrod'},
    'Uranus': {'distance': 19.22, 'size': 0.04, 'color': 'lightblue'},
    'Neptune': {'distance': 30.05, 'size': 0.04, 'color': 'blue'}
}

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the Sun and planets
for planet, data in planets.items():
    ax.scatter(data['distance'], 0, 0, s=data['size']*1000, color=data['color'], label=planet)
    
    # Plot the orbit path
    theta = np.linspace(0, 2 * np.pi, 100)
    x_orbit = data['distance'] * np.cos(theta)
    y_orbit = data['distance'] * np.sin(theta)
    z_orbit = np.zeros_like(theta)
    ax.plot(x_orbit, y_orbit, z_orbit, color=data['color'], linestyle='--')

# Labels and title
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title('Model of the Solar System with Orbits')
ax.legend()

plt.show()
