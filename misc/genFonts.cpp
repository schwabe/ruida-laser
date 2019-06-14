#define CONFIG_FONT_HERSHEY

#ifdef CONFIG_FONT_HERSHEY
#include "hershey_font.h"
#else
#include "asteroids_font.h"
#endif

#include <iostream>

int lastx = -1;
int lasty = -1;
bool in_line=false;

void moveto(int x, int y)
{
  
  lastx = x;
  lasty = y;
  //std::cout << "move to " << std::to_string(x) << ", " << std::to_string(y) << std::endl;

  if (in_line)
    std::cout << "], ";
  in_line = false;
}

void lineto(int x, int y)
{
  if (!in_line)
    std::cout << "[";
  else
    std::cout << ", ";
  //std::cout << "line to " << std::to_string(x) << ", " << std::to_string(y) <<" " << std::to_string(in_line) << std::endl;
  if (!in_line)
    std::cout << "(" << lastx << "," << lasty << "), ";
  std::cout << "(" << x << "," << y << ")" ;
  lastx = x;
  lasty = y;
  in_line = true;

}

int
draw_character(
	       char c,
	       int x,
	       int y,
	       int size
	       )
{
#ifdef CONFIG_FONT_HERSHEY
  const hershey_char_t * const f = &hershey_simplex[c - ' '];
  int next_moveto = 1;

  for(int i = 0 ; i < f->count ; i++)
    {
      int dx = f->points[2*i+0];
      int dy = f->points[2*i+1];
      if (dx == -1)
	{
	  next_moveto = 1;
	  continue;
	}

      dx = (dx * size) * 3 / 4;
      dy = (dy * size) * 3 / 4;

      if (next_moveto)
	moveto(x + dx, y + dy);
      else
	lineto(x + dx, y + dy);

      next_moveto = 0;
    }

  return (f->width * size) * 3 / 4;
#else
  // Asteroids font only has upper case
  if ('a' <= c && c <= 'z')
    c -= 'a' - 'A';

  const uint8_t * const pts = asteroids_font[c - ' '].points;
  int next_moveto = 1;

  for(int i = 0 ; i < 8 ; i++)
    {
      uint8_t delta = pts[i];
      if (delta == FONT_LAST)
	break;
      if (delta == FONT_UP)
	{
	  next_moveto = 1;
	  continue;
	}

      unsigned dx = ((delta >> 4) & 0xF) * size;
      unsigned dy = ((delta >> 0) & 0xF) * size;

      if (next_moveto)
	moveto(x + dx, y + dy);
      else
	lineto(x + dx, y + dy);

      next_moveto = 0;
    }

  return 12 * size;
#endif
}

int
main(int argc, char** argv)
{
#ifdef CONFIG_FONT_HERSHEY
  std::cout  << "hershey = {" << std::endl;
#else
  std::cout  << "asteroids = {" << std::endl;
#endif
  for (char c=' '; c <= 'z'; c++)
    {
      auto cs = std::string(1,c);
      if (c == '\\')
	cs = "\\\\";
      else if (c == '\'')
	cs = "\"'\"";
      
      std::cout <<"'" << cs << "': [";
      draw_character(c, 0,0, 100);
      std::cout << "]], " << std::endl;
      in_line=false;
    }
  std::cout << "}" << std::endl;
  return 0;
}


