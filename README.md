# Count Genies
##### By Hagai Hargil

##### Purpose: Analysis of video to determine how many Genies were grabbed.

#### General code structure:
1. `main_GenieCounter.py` receives filename of the video or device ID of camera, alongside the drawer number (currently 1-7).
2. Every 10 frames (currently, can obviously be changed) the script checks if the frame is stable, meaning that there hasn't been a signficant change in the last 10 frames. This happens after a drawer was pulled open, and someone is about to grab hold of a Genie.
3. If the video is indeed "stable" the code tries to count the circles in the image and stores it.
4. The number of grabbed Genies is the maximal number of Genies that the script has the detected (=initial number of cans) minus the last number of circles it successfully counted. This output is returned to the user. 

### Caveats
1. "Stability of frames" - This is tricky, as someone might open a drawer and immediately grab a Genie, making all frames unstable. We can avoid it by changing the number of frames we skip (currently 10), increasing the threshold of similar frames (so less-alike frames will still be counted as similar) or some other fancy algorithm. The best way to find the ideal number is to take several more videos of people grabbing Genies and see how much time it takes. A different approach would be to have a screen (or a sound) to indicate to the hungry person that he should wait for the algorithm to count Genies (we're talking about half a second).

2. Threshold of similar frames - This number has been set tentatively as well, and should be verified using more footage. It's located in `findStableFrame.py`. It should definitely be changed of the resolution of the videos change - any changes to image format should be addressed for in this script, and in `numOfCircles.py`.

3. Size of circles - Only the minimal and maximal radii of circles for drawer 2 (=second drawer from the top) were verified. You should film the opening of each drawer, and make sure that the values there do actually fit the image received. The other parameters in `numOfCircles.py` besides the minimal and maximal radii of the circles should generally not be changed.

While I'm sure this script won't work right from the start for all drawers and all scenarios, I do believe this is a good place to start. I also provided a simple testing script called `countGeniesExample.py` that should help you determine the right size of circles for the opening of all drawers, giving the right frames.
