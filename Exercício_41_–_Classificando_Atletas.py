{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Exercício 41 – Classificando Atletas",
      "provenance": [],
      "authorship_tag": "ABX9TyOZZ+SqjCTXJLCpuiJs7fnl",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/samucale/Curso-em-vd-Python/blob/main/Exerc%C3%ADcio_41_%E2%80%93_Classificando_Atletas.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bbb1-H2ejnTW"
      },
      "source": [
        "*Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:\n",
        "\n",
        "– Até 9 anos: MIRIM\n",
        "\n",
        "– Até 14 anos: INFANTIL\n",
        "\n",
        "– Até 19 anos: JÚNIOR\n",
        "\n",
        "– Até 25 anos: SÊNIOR\n",
        "\n",
        "– Acima de 25 anos: MASTER*"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "udp1D6exjj3X",
        "outputId": "b9ee5fef-2d9d-4957-c66f-be2e49a0b8c8"
      },
      "source": [
        "from datetime import date\n",
        "atual = date.today().year\n",
        "nascimento = int(input('Ano de nascimento: '))\n",
        "idade = atual - nascimento\n",
        "print ('O atleta tem {} anos.'.format(idade))\n",
        "if idade <= 9:\n",
        "  print ('Classificacão : MIRIM')\n",
        "elif idade <= 14:\n",
        "  print ('Classificação : INFANTIL')\n",
        "elif idade <= 19:\n",
        "  print ('Classificação: JUNIOR')\n",
        "elif idade <= 25: \n",
        "  print ('Classificação : SENIOR')\n",
        "else :\n",
        "  print ('Classificação MASTER')\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Ano de nascimento: 2016\n",
            "O atleta tem 5 anos.\n",
            "Classificacão : MIRIM\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p-V4smVanPAl"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}