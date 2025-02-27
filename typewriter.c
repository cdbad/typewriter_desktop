// /usr/local/bin

#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int fb = open("/dev/fb0", O_RDWR);
    if (fb < 0) {
        perror("Error opening framebuffer");
        return 1;
    }

    // Get screen dimensions
    struct fb_var_screeninfo vinfo;
    ioctl(fb, FBIOGET_VSCREENINFO, &vinfo);
    int fb_width = vinfo.xres;
    int fb_height = vinfo.yres;
    int fb_bpp = vinfo.bits_per_pixel;
    int fb_bytes = fb_bpp / 8;

    // Map screen into memory
    int fb_data_size = fb_width * fb_height * fb_bytes;
    char *fbdata = mmap(
        0,
        fb_data_size, 
        PROT_READ | PROT_WRITE,
        MAP_SHARED,
        fb,
        (off_t)0
    );

    // Blank screen
    memset (fbdata, 255, fb_data_size);

    //Tidy up
    munmap (fbdata, fb_data_size);
    close (fb);

    return 0;
}
