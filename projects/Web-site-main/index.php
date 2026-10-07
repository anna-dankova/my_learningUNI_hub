<?php include 'header.php'; ?>

<main>
<h1 class="visually-hidden">Seminarska naloga</h1>
<h2 class="visually-hidden">My travel website</h2>

<div id="glavniKarousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
    <div class="carousel-indicators">
        <button type="button" data-bs-target="#glavniKarousel" data-bs-slide-to="0" class="active"></button>
        <button type="button" data-bs-target="#glavniKarousel" data-bs-slide-to="1"></button>
        <button type="button" data-bs-target="#glavniKarousel" data-bs-slide-to="2"></button>
    </div>
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="img/img_japonska.jpg" class="d-block w-100" alt="Japan">
            <div class="carousel-caption">
                <h3>Japan</h3>
                <p>Tokyo – The City of the Future</p>
            </div>
        </div>
        <div class="carousel-item">
            <img src="img/img_SouthKorea2.jpg" class="d-block w-100" alt="South Korea">
            <div class="carousel-caption">
                <h3>South Korea</h3>
                <p>Seoul – Where Tradition Meets Modernity</p>
            </div>
        </div>
        <div class="carousel-item">
            <img src="img/img_NY.jpg" class="d-block w-100" alt="USA">
            <div class="carousel-caption">
                <h3>United States</h3>
                <p>New York – The City That Never Sleeps</p>
            </div>
        </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#glavniKarousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon"></span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#glavniKarousel" data-bs-slide="next">
        <span class="carousel-control-next-icon"></span>
    </button>
</div>

<section class="container mt-5">

    <h2>Countries I Want to Visit</h2>
    <table class="table table-bordered table-striped mt-3">
        <thead class="table-dark">
            <tr>
                <th>Country</th>
                <th>Capital</th>
                <th>Language</th>
                <th>Currency</th>
                <th>Continent</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>South Korea</td><td>Seoul</td><td>Korean</td><td>Won (₩)</td><td>Asia</td></tr>
            <tr><td>Japan</td><td>Tokyo</td><td>Japanese</td><td>Yen (¥)</td><td>Asia</td></tr>
            <tr><td>China</td><td>Beijing</td><td>Mandarin</td><td>Yuan (¥)</td><td>Asia</td></tr>
            <tr><td>United States</td><td>Washington D.C.</td><td>English</td><td>Dollar ($)</td><td>North America</td></tr>
            <tr><td>England</td><td>London</td><td>English</td><td>Pound (£)</td><td>Europe</td></tr>
            <tr><td>Norway</td><td>Oslo</td><td>Norwegian</td><td>Krone (kr)</td><td>Europe</td></tr>
            <tr><td>Australia</td><td>Canberra</td><td>English</td><td>Dollar (A$)</td><td>Oceania</td></tr>
            <tr><td>Thailand</td><td>Bangkok</td><td>Thai</td><td>Baht (฿)</td><td>Asia</td></tr>
            <tr><td>New Zealand</td><td>Wellington</td><td>English</td><td>Dollar (NZ$)</td><td>Oceania</td></tr>
            <tr><td>Philippines</td><td>Manila</td><td>Filipino</td><td>Peso (₱)</td><td>Asia</td></tr>
        </tbody>
    </table>

    <h2 class="mt-5">Countries I Have Already Visited</h2>
    <table class="table table-bordered table-striped mt-3">
        <thead class="table-dark">
            <tr>
                <th>Country</th>
                <th>Capital</th>
                <th>Best Time to Visit</th>
                <th>Top Attraction #1</th>
                <th>Top Attraction #2</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Hong Kong</td><td>Hong Kong</td><td>October – December</td><td>Victoria Peak</td><td>Tian Tan Buddha</td></tr>
            <tr><td>Thailand</td><td>Bangkok</td><td>November – February</td><td>Grand Palace</td><td>Phi Phi Islands</td></tr>
            <tr><td>Singapore</td><td>Singapore</td><td>February – April</td><td>Gardens by the Bay</td><td>Marina Bay Sands</td></tr>
            <tr><td>Russia</td><td>Moscow</td><td>May – September</td><td>Red Square</td><td>Lake Baikal</td></tr>
            <tr><td>France</td><td>Paris</td><td>April – June</td><td>Eiffel Tower</td><td>Louvre Museum</td></tr>
            <tr><td>Uzbekistan</td><td>Tashkent</td><td>March – May</td><td>Registan Square</td><td>Bukhara Old City</td></tr>
            <tr><td>Turkey</td><td>Ankara</td><td>April – May</td><td>Hagia Sophia</td><td>Cappadocia</td></tr>
            <tr><td>Egypt</td><td>Cairo</td><td>October – April</td><td>Pyramids of Giza</td><td>Luxor Temple</td></tr>
            <tr><td>Malaysia</td><td>Kuala Lumpur</td><td>March – October</td><td>Petronas Towers</td><td>Batu Caves</td></tr>
            <tr><td>Italy</td><td>Rome</td><td>May – June</td><td>Colosseum</td><td>Vatican</td></tr>
        </tbody>
    </table>

</section>

</main>

<?php include 'footer.php'; ?>
