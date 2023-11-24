#pragma once

#include "math.h"

/**
 * @brief inventory of a climber
 * TODO: jak tohle okomentovat? 
 * 
 */
typedef struct inventory
{
      /* data */
      bool climbing_guide;

      /* !!! ROPES !!! */
      bool rope;
      int length_rope;

      /* !!! PROTECTION !!! */
      bool hammer;
      int pit_1;
      int pit_2;
      int pit_3;
      int pit_4;
      int pit_5;

      int wed_1;
      int wed_2;
      int wed_3;
      int wed_4;
      int wed_5;

      int cam_1;
      int cam_2;
      int cam_3;
      int cam_4;
      int cam_5;

      int carabiners;
} inventory_t;

 
/**
 * @brief character of a climber
 * 
 */
typedef struct climber 
{
      bool is_alive;
      int health;
      int tiredness;

      int strength;
      int technique;
      int protection_placing;
      int rope_management;
      inventory_t inventory;
} climber_t;


typedef struct protection_possibility
{
      /* data */
      bool is_artificial;

      float crack_width;
};


typedef struct climbing_section
{
      /* data */
      int length;
      int strg_diff;
      int tech_diff;

      bool is_protected;
      protection_possibility protection;      
};


typedef struct single_pitch {
      int no_sections;
      /* TODO: jak udelat nekolik climbing sections v jedny singlepitch. obdobne pak multipitch*/
} single_pitch_t;


typedef struct location {
      int NEVIM;
} location_t;

enum Places {Aljazev dom, Triglav, Blllaaa}
