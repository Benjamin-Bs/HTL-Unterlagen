import { AfterViewInit, Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { RangeCustomEvent } from '@ionic/angular';
import { BoxGeometry, Mesh, MeshBasicMaterial, PerspectiveCamera, Scene, WebGLRenderer } from 'three';

@Component({
  selector: 'app-threejs-demo',
  templateUrl: './threejs-demo.component.html',
  styleUrls: ['./threejs-demo.component.scss'],
})
export class ThreejsDemoComponent implements OnInit, AfterViewInit {

  @ViewChild('threejs')
  canvas!: ElementRef<HTMLCanvasElement>;
  scene!: Scene;
  camera!: PerspectiveCamera;
  renderer!: WebGLRenderer;
  cube!: Mesh<BoxGeometry, MeshBasicMaterial>;
  rotationSpeed: number = 0

  constructor() { }

  ngOnInit() { }

  ngAfterViewInit(): void {
    this.scene = new Scene();
    this.camera = new PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

    this.renderer = new WebGLRenderer({ canvas: this.canvas.nativeElement });
    this.renderer.setSize(window.innerWidth, window.innerHeight);

    const geometry = new BoxGeometry(1, 1, 1);
    const material = new MeshBasicMaterial({ color: 0x9932CC });
    this.cube = new Mesh(geometry, material);
    this.scene.add(this.cube);

    this.camera.position.z = 5;
    this.renderer.setAnimationLoop(() => this.animate());
  }

  animate() {
    this.cube.rotation.x += this.rotationSpeed * 0.01;
    this.cube.rotation.y += this.rotationSpeed * 0.01;
    this.renderer.render(this.scene, this.camera);
  }

  onRotationSpeedChanged(ev: Event){
    const rangeEvent = ev as RangeCustomEvent;
    this.rotationSpeed = rangeEvent.detail.value as number;
  }

}
