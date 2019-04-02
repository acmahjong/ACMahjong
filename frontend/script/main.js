var renderer = new THREE.WebGLRenderer();
var w = Math.min(window.innerWidth, window.innerHeight * 1.7777);
var h = Math.min(window.innerHeight, window.innerWidth / 1.7777);
renderer.setSize(w, h);
console.log(w, h);
var element = document.body.appendChild(renderer.domElement);
element.style.margin = "auto"
element.style.position = "absolute";
element.style.top = 0;
element.style.left = 0;
element.style.bottom = 0;
element.style.right = 0;

playerScene();
function render() {
    requestAnimationFrame(render);  
    renderer.render(scene, camera);
}
render();

