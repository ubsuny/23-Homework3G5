{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNureZVHTdQqg1chx24gqSR",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AhmedCode99/projectile/blob/main/projectile_module.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Nt2kNUoqwPyl"
      },
      "outputs": [],
      "source": [
        "def projectile_with_drag(v_start): # Insert the starting velocity\n",
        "  import math\n",
        "  import matplotlib.pyplot as plt\n",
        "\n",
        "\n",
        "  g = 9.81 # m / s^2\n",
        "  dt = 0.5 # time step in seconds\n",
        "\n",
        "  x_start = 0 # starting x position\n",
        "  y_start = 0 #starting y position\n",
        "\n",
        "  const = 4*(10**-5) # Air Drag B_2 constant (1 / meter)\n",
        "\n",
        "  v_initial = v_start # meters per second\n",
        "\n",
        "  angle_degree = [30,35,40,45,50,55] # launch angle in degree\n",
        "  angle = [math.radians(degrees) for degrees in angle_degree] #convert launch angle to radians\n",
        "\n",
        "  x_list=[] #list to store x postions\n",
        "  y_list=[] #list to store y postions\n",
        "\n",
        "  for j in range(len(angle)): # loop over launch angles\n",
        "\n",
        "    vx = v_initial*math.cos(angle[j]) # intial x velocity\n",
        "    vy = v_initial*math.sin(angle[j]) # initial y velocity\n",
        "\n",
        "    x=[x_start] # list to store x postions\n",
        "    y=[y_start] # list to store y postions\n",
        "\n",
        "    i = 0 # index for while loop\n",
        "\n",
        "    while y[-1]>=0: # loop to calculate x and y positions\n",
        "      x.append(x[i]+vx*dt) # calculate and save x\n",
        "      y.append(y[i]+vy*dt) # calculate and save y\n",
        "      vx=vx-const*dt*vx*math.sqrt((vx**2)+(vy**2)) # update x velocity\n",
        "      vy=vy-dt*(g+const*vy*math.sqrt((vx**2)+(vy**2))) # update y velocity\n",
        "      i=i+1 # update index\n",
        "\n",
        "    #interpolate between last two points to determine final position\n",
        "    r = -y[-2]/y[-1]\n",
        "    x[-1] = (x[-2]+r*x[-1])/(r+1)\n",
        "    y[-1]=0.0\n",
        "\n",
        "    # saving x and y positions\n",
        "    x_list.append(x)\n",
        "    y_list.append(y)\n",
        "\n",
        "  #plotting\n",
        "\n",
        "  colours=[\"purple\",\"blue\",\"green\",\"yellow\",\"orange\",\"red\"] # list of colours\n",
        "  plt.figure(figsize=(8,6)) # set plot size\n",
        "  for i in range(len(x_list)): # plotting trajectory for each launch angle\n",
        "      plt.scatter(list(map(lambda z: z/1000, x_list[i])),list(map(lambda z: z/1000, y_list[i])), # converting from m to km\n",
        "                  c=colours[i],s=1,label='θ = {}°'.format(angle_degree[i])) # colours and legends\n",
        "  plt.xlabel('x (km)')\n",
        "  plt.ylabel('y (km)')\n",
        "  plt.legend()\n",
        "  plt.title(\"Projectile Motion with Air Drag\")\n",
        "  plt.show()\n",
        "  return plt"
      ]
    }
  ]
}