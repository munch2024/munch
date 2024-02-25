import { ReactComponent as QuiGon } from './qui-gon.svg';
import { ReactComponent as ObiWan } from './obi-wan.svg';
import { ReactComponent as ObiWanOld } from './obi-hilt-old.svg';
import { ReactComponent as DarthMaul } from './darth-maul-hilt.svg';
import { ReactComponent as AhsokaHilt } from './ahsoka-hilt.svg';
import { ReactComponent as AnakinHilt } from './anakin-hilt.svg';
import { ReactComponent as VaderHilt } from './darth-vader-hilt.svg';
import { ReactComponent as KyloHilt } from './kylo-ren-hilt.svg';
import './App.css';

function App() {
  
  const [nonChosen, setNonChosen] = useState(true);
  const [blue, setBlue] = useState(false);
  const [red, setRed] = useState(false);
  const [green, setGreen] = useState(false);
  const [purple, setPurple] = useState(false);
  const [yellow, setYellow] = useState(false);
  const [white, setWhite] = useState(false);

  const [saberOne, setSaberOne] = useState(true);
  const [doubleSaber, setDoubleSaber] = useState(false);
  const [quiGon, setQuiGon] = useState(false);
  const [obiWanNew, setObiWanNew] = useState(false);
  const [obiWanOld, setObiWanOld] = useState(false);
  const [ahsoka, setAhsoka] = useState(false);
  const [anakinHilt, setAnakinHilt] = useState(false);
  const [vaderHilt, setVaderHilt] = useState(false);
  const [kyloHilt, setKyloHilt] = useState(false);


  return (
    <div className="App">

          {/* Colors */}

          <button className="testsub" onClick={() => {setGreen(true); setWhite(false); setYellow(false); setPurple(false); setRed(false); setBlue(false); setNonChosen(false);}}>Green
          </button> 

          <button className="testsub" onClick={() => {setBlue(true); setWhite(false); setYellow(false); setPurple(false); setRed(false); setGreen(false); setNonChosen(false);}}>Blue
          </button>

          <button className="testsub" onClick={() => {setRed(true); setWhite(false); setYellow(false); setPurple(false); setBlue(false); setGreen(false); setNonChosen(false);}}>Red
          </button>

          <button className="testsub" onClick={() => {setPurple(true); setWhite(false); setYellow(false); setGreen(false);  setRed(false); setBlue(false); setNonChosen(false);}}>Purple
          </button> 

          <button className="testsub" onClick={() => {setYellow(true); setWhite(false); setPurple(false); setGreen(false);  setRed(false); setBlue(false); setNonChosen(false);}}>Yellow
          </button> 

          <button className="testsub" onClick={() => {setWhite(true); setYellow(false); setPurple(false); setGreen(false);  setRed(false); setBlue(false); setNonChosen(false);}}>White
          </button> 
          
          <br />

          {/* Hilts */}

          <button className="testsub" onClick={() => {setDoubleSaber(true); setKyloHilt(false); setVaderHilt(false); setAnakinHilt(false); setAhsoka(false); setSaberOne(false); setQuiGon(false); setObiWanNew(false); setObiWanOld(false);}}>Darth Maul
          </button>

          <button className="testsub" onClick={() => {setQuiGon(true); setKyloHilt(false); setVaderHilt(false); setAnakinHilt(false); setAhsoka(false); setDoubleSaber(false); setSaberOne(false); setObiWanNew(false); setObiWanOld(false);}}>Qui Gon
          </button>

          <button className="testsub" onClick={() => {setObiWanNew(true); setKyloHilt(false); setVaderHilt(false); setAnakinHilt(false); setAhsoka(false); setDoubleSaber(false); setSaberOne(false); setQuiGon(false); setObiWanOld(false);}}>Obi Wan
          </button>

          <button className="testsub" onClick={() => {setObiWanOld(true); setKyloHilt(false); setVaderHilt(false); setAnakinHilt(false); setAhsoka(false); setDoubleSaber(false); setSaberOne(false); setQuiGon(false); setObiWanNew(false);}}>Obi Wan Old
          </button>

          <button className="testsub" onClick={() => {setAhsoka(true); setKyloHilt(false); setVaderHilt(false); setAnakinHilt(false); setObiWanOld(false); setDoubleSaber(false); setSaberOne(false); setQuiGon(false); setObiWanNew(false);}}>Ahsoka Tano
          </button>

          <button className="testsub" onClick={() => {setAnakinHilt(true); setKyloHilt(false); setVaderHilt(false); setAhsoka(false); setObiWanOld(false); setDoubleSaber(false); setSaberOne(false); setQuiGon(false); setObiWanNew(false);}}>Anakin
          </button>

          <button className="testsub" onClick={() => {setVaderHilt(true); setKyloHilt(false); setAnakinHilt(false); setAhsoka(false); setObiWanOld(false); setDoubleSaber(false); setSaberOne(false); setQuiGon(false); setObiWanNew(false);}}>Vader
          </button>

          <button className="testsub" onClick={() => { setKyloHilt(true);setVaderHilt(false); setAnakinHilt(false); setAhsoka(false); setObiWanOld(false); setDoubleSaber(false); setSaberOne(false); setQuiGon(false); setObiWanNew(false);}}>Kylo
          </button>


<div class="lightsaber">
  <input type="checkbox" id="on-off" />
          {nonChosen && (
            <>
            <div className="blade colol"></div>
            {/* <div className="blade2 colol"></div> */}
            </>
          )}

          {blue && (
          <div className="blade colol2"></div>
          )}

          {red && (
          <div className="blade red-clr"></div>
          )}

          {green && (
          <div className="blade colol"></div>
          )}

          {purple && (
          <div className="blade purple-clr"></div>
          )}

          {yellow && (
          <div className="blade yellow-clr"></div>
          )}

          {white && (
          <div className="blade white-clr"></div>
          )}


        {saberOne && (
              <label className="hilt" for="on-off">
              <QuiGon />
            </label>
          )}

        {doubleSaber && (
          <>
            <div className="blade2 colol"></div>
            <label className="hilt" for="on-off">
              <DarthMaul />
            </label>
            </>
          )}

        {quiGon && (
              <label className="hilt" for="on-off">
              <QuiGon />
            </label>
          )}

        {obiWanNew && (
              <label className="hilt" for="on-off">
              <ObiWan />
            </label>
          )}

        {obiWanOld && (
              <label className="hilt" for="on-off">
              <ObiWanOld />
            </label>
          )}

        {ahsoka && (
              <label className="hilt" for="on-off">
              <AhsokaHilt />
            </label>
          )}

        {anakinHilt && (
              <label className="hilt" for="on-off">
              <AnakinHilt />
            </label>
          )}

        {vaderHilt && (
              <label className="hilt" for="on-off">
              <VaderHilt />
            </label>
          )}

        {kyloHilt && (
            //   <label className="hilt" for="on-off">
            //   <KyloHilt className="hilt2"/>
            // </label>
            <>
            <div className="blade3 colol"></div>
            <div className="blade4 colol"></div>
            <label className="hilt" for="on-off">
              <KyloHilt className="hilt2"/>
            </label>
            </>
          )}

</div>


<div className="infobox">
          {nonChosen && (
            <div>Yoyoyo</div>
          )}

          {blue && (
          <div>aasdsd</div>
          )}

          {green && (
          <div>fgfgfg</div>
          )}

</div>

    </div>
  );
}

export default App;
