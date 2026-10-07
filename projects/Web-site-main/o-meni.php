<?php include 'header.php'; ?>

<main style="min-height: calc(100vh - 200px); display: flex; flex-direction: column;">

<section class="container mt-5 flex-grow-1">
    <div class="card page-card glass-effect" style="min-height: 70vh; display: flex; flex-direction: column;">
        <div class="page-header">
            <h1 class="mb-0">About Me</h1>
        </div>
        
        <div class="card-body p-5 flex-grow-1 d-flex flex-column">
            
            <div class="row align-items-center mb-5">
                <div class="col-md-4 text-center mb-4 mb-md-0">
                    <img src="img/img_jaz1.jpg" class="profile-img mx-auto shadow-lg" style="width: 260px; object-fit: contain;" alt="Anna Dankova">
                </div>
                <div class="col-md-8">
                    <p class="display-5 fw-bold mb-3" style="color:#6a6969;">Anna Dankova</p>
                    <h4 class="text-muted mb-4" style="color: #7f7e7e;">Student ID: 35250060</h4>
                </div>
            </div>
            
            <div class="row flex-grow-1">
        <div class="col-lg-8 mx-auto">
            <div class="lh-lg" style="font-size: 0.9rem; line-height: 1.7;">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.</p>
                <p>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet.</p>
                <p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident.</p>
            </div>
        </div>
    </div>
            
            <div class="row mt-5">
                <div class="col-md-6">
                    <h3>My Favourite Websites</h3>
                    <ul class="list-unstyled">
                        <li><a href="https://www.youtube.com" target="_blank">•YouTube</a></li>
                        <li><a href="https://www.spotify.com" target="_blank">•Spotify</a></li>
                        <li><a href="https://doramy.club" target="_blank">•Doramy Club</a></li>
                        <li><a href="https://kinogo.la" target="_blank">•Kinogo</a></li>
                        <li><a href="https://www.netflix.com" target="_blank">•Netflix</a></li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <h3>My Favourite Movies</h3>
                    <ul class="list-unstyled">
                        <li>•Spirited Away (2001)</li>
                        <li>•Parasite (2019)</li>
                        <li>•Iron Man (2008)</li>
                        <li>•Your Name (2016)</li>
                        <li>•Guardians of the Galaxy (2014)</li>
                    </ul>
                </div>
            </div>

            <h3 class="mt-5 mb-4">My Travel Wishlist</h3>
            <div class="table-responsive">
                <table class="table table-bordered table-striped">
                    <thead class="table-dark">
                        <tr>
                            <th>Country</th>
                            <th>City</th>
                            <th>Reason to Visit</th>
                            <th>National Dish</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>Japan</td><td>Tokyo</td><td>Culture and food</td><td>Sushi</td><td>Raw fish on seasoned rice, fresh and delicate</td></tr>
                        <tr><td>South Korea</td><td>Seoul</td><td>K-dramas and K-pop</td><td>Bibimbap</td><td>Mixed rice bowl with vegetables, egg and chili paste</td></tr>
                        <tr><td>Norway</td><td>Oslo</td><td>Northern lights</td><td>Rakfisk</td><td>Fermented trout, traditional winter delicacy</td></tr>
                        <tr><td>New Zealand</td><td>Wellington</td><td>Nature and landscapes</td><td>Hangi</td><td>Meat and vegetables slow-cooked underground on hot stones</td></tr>
                        <tr><td>Australia</td><td>Sydney</td><td>Opera House and beaches</td><td>Meat Pie</td><td>Flaky pastry filled with minced meat and gravy</td></tr>
                    </tbody>
                </table>
            </div>

        </div>
        
    </div>

</section>

</main>

<?php include 'footer.php'; ?>
